import logging
from pydantic import BaseModel, Field, PrivateAttr
from ._utils import JinjaVariables, render_jinja
from typing import Any, Dict, Union
from ._timeslice import Timeslice

# from databricks.sdk.runtime import spark
import os


class DeltaLake(BaseModel):
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self._logger = logging.getLogger(self.__class__.__name__)
        self._render()
        self.create_table()

    _logger: Any = PrivateAttr(default=None)
    _replacements: Dict[JinjaVariables, str] = PrivateAttr(default=None)
    database: str = Field(...)
    destination_table: str = Field(...)
    table: str = Field(...)
    container: str = Field(...)
    root: str = Field(...)
    path: str = Field(...)
    options: Union[dict, None] = Field(default=None)
    timeslice: Timeslice = Field(...)
    location: str = Field(default=None)
    checkpoint: str = Field(default=None)

    def _render(self):
        self._replacements = {
            JinjaVariables.TABLE: self.destination_table,
            JinjaVariables.DATABASE: self.database,
            JinjaVariables.CONTAINER: self.container,
            JinjaVariables.CHECKPOINT: self.checkpoint,
        }

        self.root = render_jinja(self.root, self._replacements)
        self.path = render_jinja(self.path, self._replacements)
        self.database = render_jinja(self.database, self._replacements)
        self.table = render_jinja(self.table, self._replacements)
        if self.options:
            for option, value in self.options.items():
                self.options[option] = render_jinja(value, self._replacements)

        self.location = os.path.join(self.root, self.path)

    def create_table(self):
        try:
            spark.sql(f"CREATE DATABASE IF NOT EXISTS `{self.database}`")  # noqa F821
            spark.sql(  # noqa F821
                f"""
                    CREATE TABLE IF NOT EXISTS `{self.database}`.`{self.table}`
                    USING DELTA
                    LOCATION '{self.location}'
                    """
            )
        except NameError:
            version = os.getenv("DATABRICKS_RUNTIME_VERSION", None)
            if version:
                raise Exception("Spark undefined on databricks runtime!")
            logging.warning(
                "spark is not defined, skipping Spark operation for testing purposes"
            )
