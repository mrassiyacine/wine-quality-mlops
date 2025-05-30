import os

import joblib
import pandas as pd
from sklearn.linear_model import ElasticNet

from src.winequalitymlops import logger
from src.winequalitymlops.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        """
        Trains the model using the training data and saves the model to the specified path.

        """
        try:
            logger.info("Starting model training...")
            train_data = pd.read_csv(self.config.train_data_path)
            train_data = train_data.drop(columns=["Id"], errors="ignore")
            X = train_data.drop(columns=[self.config.target_column])
            y = train_data[self.config.target_column]

            model = ElasticNet(
                alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42
            )
            model.fit(X, y)

            joblib.dump(
                model, os.path.join(self.config.root_dir, self.config.model_name)
            )
            logger.info(
                f"Model trained and saved at {self.config.root_dir}/{self.config.model_name}"
            )
            return model
        except Exception as e:
            logger.exception(f"An error occurred during model training: {e}")
            raise e
