from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from vectice.models.resource.base import Resource
from vectice.models.resource.metadata import DatasetSourceOrigin
from vectice.models.resource.metadata.column_metadata import DBColumn
from vectice.models.resource.metadata.db_metadata import DBMetadata, MetadataDB

if TYPE_CHECKING:
    from google.cloud.bigquery import Client as BQClient
    from google.cloud.bigquery import Table

_logger = logging.getLogger(__name__)


class BigQueryResource(Resource):
    """Wrap columnar data and its metadata in BigQuery.

    Vectice stores metadata -- data about your dataset -- communicated
    with a resource.  Your actual dataset is not stored by Vectice.

    This resource wraps data that you have stored in BigQuery. You assign it to a step.

    ```python
    from vectice import BigQueryResource
    from google.cloud.bigquery import Client

    my_service_account_file = "MY_SERVICE_ACCOUNT_JSON_PATH"  # (1)
    bq_client = Client.from_service_account_json(json_credentials_path=my_service_account_file)  # (2)
    bq_resource = BigQueryResource(
        bq_client,
        table="bigquery-public-data.stackoverflow.posts_questions",
    )
    ```

    1. See [Service account credentials](https://developers.google.com/workspace/guides/create-credentials#service-account).
    1. See [GCS docs](https://cloud.google.com/python/docs/reference/storage/latest/modules).

    Note that these three concepts are distinct, even if easily conflated:

    * Where the data is stored
    * The format at rest (in storage)
    * The format when loaded in a running Python program

    Notably, the statistics collectors provided by Vectice operate
    only on this last and only in the event that the data is loaded as
    a pandas dataframe.
    """

    _origin = DatasetSourceOrigin.BIGQUERY.value

    def __init__(
        self,
        bq_client: BQClient,
        path: str,
    ):
        """Initialize a BigQuery resource.

        Parameters:
            bq_client: The `google.cloud.bigquery.Client` used
                to interact with BigQuery.
            path: The path to retrieve the dataset or the table.
        """
        super().__init__()
        self.path = path
        self.bq_client = bq_client

    def _fetch_data(self) -> dict[str, Table | None]:
        from google.api_core.exceptions import Forbidden

        count_dots_in_path = self.path.count(".")
        is_dataset = count_dots_in_path == 1
        is_table = count_dots_in_path == 2

        if is_table is True:
            table_name = self.path.rpartition(".")[-1]
            tb = None
            try:
                tb = self.bq_client.get_table(table=self.path)
            except Forbidden:
                _logger.warning(f"Failed to fetch data information for table {table_name}")
                pass

            return {table_name: tb}

        if is_dataset is True:
            tables_dict: dict[str, Table | None] = {}
            try:
                tables = self.bq_client.list_tables(dataset=self.path)
                for table in tables:
                    try:
                        tables_dict[table.table_id] = self.bq_client.get_table(table=f"{self.path}.{table.table_id}")
                    except Exception:
                        _logger.warning(f"Failed to fetch data information for table {table.table_id}")
                        tables_dict[table.table_id] = None
                        continue
                return tables_dict
            except Forbidden:
                _logger.warning(f"Failed to list tables for dataset {self.path}")
                return {}

        raise ValueError("path is invalid, please reference either a dataset or a table.")

    def _build_metadata(self) -> DBMetadata:
        tables_metadata: dict[str, Table | None] = self.data  # type:ignore[assignment]
        dbs: list[MetadataDB] = []
        for table_name, table_metadata in tables_metadata.items():
            columns: list[DBColumn] = []
            size = None
            rows_number = None
            updated_date = None
            if table_metadata is not None:
                size = table_metadata.num_bytes
                rows_number = table_metadata.num_rows
                updated_date = table_metadata.modified.isoformat()
                for column in table_metadata.schema:
                    columns.append(
                        DBColumn(
                            name=column.name,
                            data_type=column.field_type,
                            is_unique=False,
                            nullable=column.is_nullable,
                            is_private_key=False,
                            is_foreign_key=False,
                        )
                    )

            dbs.append(
                MetadataDB(
                    name=table_name,
                    rows_number=rows_number,
                    size=size,
                    columns=columns,
                    updated_date=updated_date,
                )
            )

        metadata_size = None
        for db in dbs:
            if db.size is not None:
                if metadata_size is None:
                    metadata_size = 0
                metadata_size += db.size

        metadata = DBMetadata(
            size=metadata_size,
            origin=self._origin,
            dbs=dbs,
        )
        return metadata
