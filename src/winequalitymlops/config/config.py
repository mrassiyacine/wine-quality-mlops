import os
from pathlib import Path

from dotenv import load_dotenv

from src.winequalitymlops.constants import (CONFIG_FILE_PATH, PARAMS_FILE_PATH,
                                            SCHEMA_FILE_PATH)
from src.winequalitymlops.entity.config_entity import (
    DataIngestionConfig, DataTransformationConfig, DataValidationConfig,
    ModelEvaluationConfig, ModelTrainerConfig)
from src.winequalitymlops.utils.common import create_directories, read_yaml

load_dotenv()


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
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

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])
        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            unzip_data=Path(config.unzip_data),
            all_schema=schema,
            STATUS_FILE=config.STATUS_FILE,
        )
        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir), data_path=Path(config.data_path)
        )
        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir])
        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name,
        )
        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        schema = self.schema.TARGET_COLUMN
        params = self.params.ElasticNet
        create_directories([config.root_dir])
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            model_path=Path(config.model_path),
            test_data_path=Path(config.test_data_path),
            target_column=schema.name,
            report_file=Path(config.report_file),
            all_params=params,
            mlflow_uri=os.getenv("MLFLOW_TRACKING_URI"),
        )
        return model_evaluation_config
