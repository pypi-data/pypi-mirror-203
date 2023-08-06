import os

import polars as pl

# import pyarrow.dataset as
from pyarrow import csv
import pyarrow.parquet as pq
import pyarrow.dataset as ds
from ezt.util.config import Config
from ezt.util.exceptions import EztAuthenticationException, EztConfigException
from ezt.util.helpers import (
    get_s3_filesystem,
    prepare_s3_path,
    get_adls_filesystem,
    prepare_adls_path,
)
import deltalake as dl


def get_source(name: str, project_base_dir: str = None) -> pl.LazyFrame:
    """Get a source by name."""

    if project_base_dir:
        config = Config(project_base_dir)
    else:
        config = Config(os.getcwd())

    source_dict = config.get_source(name)

    source_getter = _get_source_getter_func(source_dict)
    return source_getter(source_dict)


def _get_source_getter_func(source_dict):
    if source_dict["filesystem"] == "s3":

        if source_dict["format"] == "parquet":
            return _get_s3_parq_source
        elif source_dict["format"] == "delta":
            return _get_s3_delta_source
        elif source_dict["format"] == "csv":
            return _get_s3_csv_source

    elif source_dict["filesystem"] == "local":

        if source_dict["format"] == "csv":
            return _get_csv_local_source
        elif source_dict["format"] == "parquet":
            return _get_parq_local_source

    elif source_dict["filesystem"] == "adls":

        if source_dict["format"] == "parquet":
            return _get_adls_parq_source
        elif source_dict["format"] == "delta":
            return _get_adls_delta_source
        elif source_dict["format"] == "csv":
            return _get_adls_csv_source


def _get_s3_parq_source(source):
    """
    Function that returns the parquet-source in s3 as a LazyFrame.
    Since lazy evaluation on remote storage not currently supported
    in polars, a dataframe is first created (read into memory) before it
    is converted to a lazyframe.
    """
    # set up s3 filesystem keys
    s3 = get_s3_filesystem()

    # removes leading and ending forwardslashes
    path = source["path"]
    if path.endswith("/"):
        path = path[:-1]

    if path.startswith("/"):
        path = path[1:]
    elif path.startswith("s3://"):
        path = path[5:]

    if source["path_type"] == "folder":
        target_path = f"s3://{path}/"
        dset = ds.dataset(target_path, format="parquet")
        table = pl.scan_ds(dset)
    elif source["path_type"] == "file":
        target_path = f"{path}"
        pa_table = pq.read_table(target_path, filesystem=s3)
        table = pl.from_arrow(pa_table).lazy()
    else:
        raise EztConfigException("Invalid or missing value for key 'path_type' in sources.yml.")

    return table


def _get_csv_local_source(source_dict):
    """Function that returns a lazyframe of a local csv-source."""
    if "csv_properties" in source_dict:
        df = pl.scan_csv(source_dict["path"], **source_dict["csv_properties"])
    else:
        df = pl.scan_csv(source_dict["path"])

    return df


def _get_parq_local_source(source_dict):
    """Function that returns a lazyframe of a local parquet-source."""
    return pl.scan_parquet(source_dict["path"])


def _get_s3_delta_source(source_dict):
    """Function that returns a lazyframe of a remote delta-source."""

    if os.getenv("AWS_ACCESS_KEY_ID") is None or os.getenv("AWS_SECRET_ACCESS_KEY") is None:
        raise EztAuthenticationException(
            "Environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY need to be set to authenticate to S3."
        )

    os.environ["AWS_S3_ALLOW_UNSAFE_RENAME"] = "true"

    if source_dict["path_type"] == "folder":
        table_path = prepare_s3_path(source_dict["path"])
    else:
        raise EztConfigException(
            'For delta-sources, the "path_type" key need to be set to "folder"'
        )

    result_lazy = pl.from_arrow(
        dl.DeltaTable(table_uri=f"{table_path}/").to_pyarrow_table()
    ).lazy()
    return result_lazy


def _get_s3_csv_source(source_dict):
    """Function that returns a lazyframe of a remote delta-source in s3."""

    path = prepare_s3_path(source_dict["path"])
    s3 = get_s3_filesystem()

    with s3.open(source_dict["path"]) as f:

        if "csv_properties" in source_dict:
            table = csv.read_csv(
                input_file=f, parse_options=csv.ParseOptions(**source_dict["csv_properties"])
            )
        else:
            table = csv.read_csv(input_file=f)

    polars_lf = pl.from_arrow(table).lazy()
    return polars_lf


def _get_adls_parq_source(source_dict):
    """Function that returns a lazyframe of a remote parquet-source in adls."""

    # set up adls filesystem keys
    adls = get_adls_filesystem()

    # removes leading and ending forwardslashes
    path = source_dict["path"]
    if path.endswith("/"):
        path = path[:-1]

    if path.startswith("/"):
        path = path[1:]
    elif path.startswith("abfss://"):
        path = path[8:]

    if source_dict["path_type"] == "folder":
        target_path = f"abfss://{path}/"
        dset = ds.dataset(target_path, format="parquet")
        table = pl.scan_ds(dset)
    elif source_dict["path_type"] == "file":
        target_path = f"{path}"
        pa_table = pq.read_table(target_path, filesystem=adls)
        table = pl.from_arrow(pa_table).lazy()
    else:
        raise EztConfigException("Invalid or missing value for key 'path_type' in sources.yml.")

    return table


def _get_adls_delta_source(source_dict):
    """Function that returns a lazyframe of a remote delta-source in adls."""

    if source_dict["path_type"] == "folder":
        table_path = prepare_adls_path(source_dict["path"])
    else:
        raise EztConfigException(
            'For delta-sources, the "path_type" key need to be set to "folder"'
        )

    result_lazy = pl.from_arrow(
        dl.DeltaTable(table_uri=f"{table_path}/").to_pyarrow_table()
    ).lazy()
    return result_lazy


def _get_adls_csv_source(source_dict):
    """Function that returns a lazyframe of a remote delta-source in s3."""

    path = prepare_adls_path(source_dict["path"])
    adls = get_adls_filesystem()

    with adls.open(source_dict["path"]) as f:

        if "csv_properties" in source_dict:
            table = csv.read_csv(
                input_file=f, parse_options=csv.ParseOptions(**source_dict["csv_properties"])
            )
        else:
            table = csv.read_csv(input_file=f)

    polars_lf = pl.from_arrow(table).lazy()
    return polars_lf
