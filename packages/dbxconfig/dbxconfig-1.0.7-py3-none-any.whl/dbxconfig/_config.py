import yaml
import os
from .dataset import DataSet
from ._timeslice import Timeslice
from ._tables import Tables, _INDEX_WILDCARD
from ._stage_type import StageType
from .dataset import dataset_factory


class Config:
    _CONFIG_PATH = "../Config/"
    _CONFIG_FILE = "config.yaml"
    _ENCODING = "utf-8"
    _TABLES = "tables"
    _SOURCE_TABLE = "source_table"

    def __init__(self, config_path: str = None):
        self.config = {}

        if not config_path:
            config_path = os.path.join(self._CONFIG_PATH, self._CONFIG_FILE)

        with open(config_path, "r", encoding=self._ENCODING) as f:
            self.config = yaml.safe_load(f)

        _tables_path = self.config["tables"]

        with open(_tables_path, "r", encoding=self._ENCODING) as f:
            self.config["tables"] = yaml.safe_load(f)

        self.tables = Tables(table_data=self.config["tables"])

    def get_table_mapping(
        self,
        timeslice: Timeslice,
        stage: StageType,
        table: str = _INDEX_WILDCARD,
        database: str = _INDEX_WILDCARD,
        index: str = None,
    ):
        table_mapping = self.tables.get_table_mapping(
            stage=stage, table=table, database=database, index=index
        )

        table_mapping.source = dataset_factory.get_data_set(
            self.config, table_mapping.source, timeslice
        )
        table_mapping.destination = dataset_factory.get_data_set(
            self.config, table_mapping.destination, timeslice
        )

        return table_mapping

    def link_checkpoint(
        self,
        source: DataSet,
        destination: DataSet,
        checkpoint_name: str = None,
    ):
        if not checkpoint_name:
            checkpoint_name = f"{source.database}.{source.table}-{destination.database}.{destination.table}"

        source.checkpoint = checkpoint_name
        source._render()
        destination.checkpoint = checkpoint_name
        destination._render()
