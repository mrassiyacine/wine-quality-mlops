from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data: Path
    STATUS_FILE: str
    all_schema: dict


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str


@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    test_data_path: Path
    target_column: str
    report_file: Path
    all_params: dict
    mlflow_uri: str
