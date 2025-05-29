import os

import pandas as pd
from sklearn.model_selection import train_test_split

from src.winequalitymlops import logger
from src.winequalitymlops.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        """
        Splits the dataset into training and testing sets and saves them as CSV files
        in the specified root directory.
        """
        try:
            logger.info("Starting train-test splitting...")
            os.makedirs(self.config.root_dir, exist_ok=True)
            data = pd.read_csv(self.config.data_path)
            train_data, test_data = train_test_split(
                data, test_size=0.25, random_state=42
            )
            logger.info(
                f"Train data shape: {train_data.shape}, Test data shape: {test_data.shape}"
            )
            train_path = os.path.join(self.config.root_dir, "train_data.csv")
            test_path = os.path.join(self.config.root_dir, "test_data.csv")
            train_data.to_csv(train_path, index=False)
            test_data.to_csv(test_path, index=False)
            logger.info("Train-test splitting completed successfully.")
            return train_path, test_path
        except Exception as e:
            logger.exception(f"An error occurred during train-test splitting: {e}")
            return None, None
