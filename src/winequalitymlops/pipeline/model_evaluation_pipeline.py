from src.winequalitymlops import logger
from src.winequalitymlops.components.model_evaluation import ModelEvaluation
from src.winequalitymlops.config.config import ConfigurationManager


class ModelEvaluationPipeline:
    def run(self):
        try:
            logger.info("Starting Model Evaluation Pipeline...")

            config_manager = ConfigurationManager()
            model_evaluation_config = config_manager.get_model_evaluation_config()

            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()

            logger.info("Model Evaluation Pipeline completed successfully.")
        except Exception as e:
            logger.exception(f"An error occurred in the Model Evaluation Pipeline: {e}")
            raise e
