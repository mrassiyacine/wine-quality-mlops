from src.winequalitymlops import logger
from src.winequalitymlops.components.data_ingestion import DataIngestion
from src.winequalitymlops.config.config import ConfigurationManager

TASK_NAME = "Data Ingestion Pipeline"


class DataIngestionPipeline:
    """
    Pipeline for data ingestion tasks.
    This class orchestrates the data ingestion process by downloading and extracting the dataset.
    """

    def initiate_data_ingestion(self):
        """
        Initiates the data ingestion process by downloading and extracting the dataset.
        """
        try:
            data_ingestion_config = ConfigurationManager().get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)

            logger.info(f"{TASK_NAME} started.")
            data_ingestion.download_data()
            logger.info("Data download completed.")
            data_ingestion.extract_zip_file()
            logger.info("Data extraction completed.")
            logger.info(f"{TASK_NAME} completed successfully.")
            return True
        except Exception as e:
            logger.exception(f"An error occurred during {TASK_NAME}: {e}")
            raise
