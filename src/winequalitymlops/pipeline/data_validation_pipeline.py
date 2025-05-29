from src.winequalitymlops import logger
from src.winequalitymlops.components.data_validation import DataValidation
from src.winequalitymlops.config.config import ConfigurationManager

TASK_NAME = "Data Validation Pipeline"


class DataValidationPipeline:
    """
    Pipeline for data validation tasks.
    This class orchestrates the data validation process by checking the schema of the dataset.
    """

    def initiate_data_validation(self):
        """
        Initiates the data validation process by validating the dataset against a predefined schema.
        """
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)

            logger.info(f"{TASK_NAME} started.")
            status = data_validation.validate_all_columns()
            if status:
                logger.info(f"{TASK_NAME} completed successfully.")
            else:
                logger.error(f"{TASK_NAME} failed. See status file for details.")
            return status
        except Exception as e:
            logger.exception(f"An error occurred during {TASK_NAME}: {e}")
            raise e
