from src.winequalitymlops import logger
from src.winequalitymlops.pipeline.data_ingestion_pipeline import \
    DataIngestionPipeline

if __name__ == "__main__":
    logger.info(
        ">>>>>>>>>>>>>>>>> Starting the Data Ingestion Pipeline... <<<<<<<<<<<<<<<<<<<<<<<"
    )
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
