from src.winequalitymlops import logger
from src.winequalitymlops.components.data_transformation import DataTransformation
from src.winequalitymlops.config.config import ConfigurationManager

TASK_NAME = "Data Transformation Pipeline"


class DataTransformationPipeline:
    """
    Pipeline for data transformation tasks.
    This class orchestrates the data transformation process by splitting the dataset.
    """

    def initiate_data_transformation(self):
        """
        Initiates the data transformation process by splitting the dataset into train and test sets.
        """
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)

            logger.info(f"{TASK_NAME} started.")
            data_transformation.train_test_splitting()
            logger.info(f"{TASK_NAME} completed successfully.")
        except Exception as e:
            logger.exception(f"An error occurred during {TASK_NAME}: {e}")
            raise
