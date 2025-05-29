from src.winequalitymlops import logger
from src.winequalitymlops.components.data_ingestion import DataIngestion
from src.winequalitymlops.config.config import ConfigurationManager

TASK_NAME = "Data Ingestion Pipeline"


class DataIngestionPipeline:
    """
    Pipeline for data ingestion tasks.
    This class orchestrates the data ingestion process by downloading and extracting the dataset.
    """

    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        """
        Initiates the data ingestion process by downloading and extracting the dataset.
        """
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)

            logger.info(f"{TASK_NAME} started.")
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
            logger.info(f"{TASK_NAME} completed.")
        except Exception as e:
            logger.exception(f"An error occurred during {TASK_NAME}: {e}")
            raise e
