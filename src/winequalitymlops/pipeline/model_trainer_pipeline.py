from src.winequalitymlops import logger
from src.winequalitymlops.components.model_trainer import ModelTrainer
from src.winequalitymlops.config.config import ConfigurationManager

TASK_NAME = "Model Trainer Pipeline"


class ModelTrainerPipeline:
    """
    Pipeline for model training tasks.
    This class orchestrates the model training process by training a machine learning model.
    """

    def initiate_model_training(self):
        """
        Initiates the model training process by training a machine learning model.
        """
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            logger.info(f"{TASK_NAME} started.")
            model_trainer.train_model()
            logger.info(f"{TASK_NAME} completed successfully.")
            return True
        except Exception as e:
            logger.exception(f"An error occurred during {TASK_NAME}: {e}")
            raise
