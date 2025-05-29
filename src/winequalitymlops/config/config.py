from pathlib import Path

from src.winequalitymlops.constants import (CONFIG_FILE_PATH, PARAMS_FILE_PATH,
                                            SCHEMA_FILE_PATH)
from src.winequalitymlops.entity.config_entity import DataIngestionConfig
from src.winequalitymlops.utils.common import create_directories, read_yaml


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        # self.params = read_yaml(params_filepath)
        # self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir),
        )
        return data_ingestion_config
