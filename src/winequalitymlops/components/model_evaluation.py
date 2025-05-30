import dagshub
import joblib
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src.winequalitymlops import logger
from src.winequalitymlops.entity.config_entity import ModelEvaluationConfig
from src.winequalitymlops.utils.common import save_json

dagshub.init(repo_owner="mrassiyacine", repo_name="wine-quality-mlops", mlflow=True)


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self, actual: pd.Series, predicted: pd.Series) -> dict:
        """
        Evaluates the model using various metrics and logs the results.
        Args:
            actual: Actual target values
            predicted: Predicted target values
        return
            Dictionary containing evaluation metrics
        """
        try:
            rmse = np.sqrt(mean_squared_error(actual, predicted))
            mae = mean_absolute_error(actual, predicted)
            r2 = r2_score(actual, predicted)
            return {"RMSE": rmse, "MAE": mae, "R2": r2}

        except Exception as e:
            logger.exception(f"An error occurred during model evaluation: {e}")
            raise e

    def log_into_mlflow(self):
        """
        Logs the model and evaluation metrics into MLflow.
        """
        try:
            test_data = pd.read_csv(self.config.test_data_path)
            test_data = test_data.drop(columns=["Id"], errors="ignore")
            X_test = test_data.drop(columns=[self.config.target_column])
            y_test = test_data[self.config.target_column]
            model = joblib.load(self.config.model_path)
            logger.info("Logging model and metrics into MLflow...")
            logger.info(f"MLflow URI: {self.config.mlflow_uri}")
            mlflow.set_tracking_uri(self.config.mlflow_uri)
            mlflow.set_experiment("Wine Quality Experiment")

            with mlflow.start_run():
                predicted_qualities = model.predict(X_test)
                metrics = self.evaluate_model(y_test, predicted_qualities)
                logger.info(f"Model evaluation scores: {metrics}")
                save_json(path=self.config.report_file, data=metrics)
                mlflow.log_params(self.config.all_params)
                for metric_name, metric_value in metrics.items():
                    mlflow.log_metric(metric_name, metric_value)

                mlflow.sklearn.log_model(model, artifact_path="model_ElasticNet")
                logger.info("Model and metrics logged into MLflow successfully.")
                return metrics
        except Exception as e:
            logger.exception(f"An error occurred while logging into MLflow: {e}")
            raise e
