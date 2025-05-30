from src.winequalitymlops import logger
from src.winequalitymlops.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.winequalitymlops.pipeline.data_transformation_pipeline import (
    DataTransformationPipeline,
)
from src.winequalitymlops.pipeline.data_validation_pipeline import (
    DataValidationPipeline,
)
from src.winequalitymlops.pipeline.model_evaluation_pipeline import (
    ModelEvaluationPipeline,
)
from src.winequalitymlops.pipeline.model_trainer_pipeline import ModelTrainerPipeline

if __name__ == "__main__":
    logger.info(
        ">>>>>>>>>>>>>>>>> Starting the Data Ingestion Pipeline... <<<<<<<<<<<<<<<<<<<<<<<"
    )
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(
        ">>>>>>>>>>>>>>>>> Data Ingestion Pipeline completed! <<<<<<<<<<<<<<<<<<<<<<<"
    )
    logger.info(
        ">>>>>>>>>>>>>>>>> Starting the Data Validation Pipeline... <<<<<<<<<<<<<<<<<<<<<<<"
    )
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info(
        ">>>>>>>>>>>>>>>>> Data Validation Pipeline completed! <<<<<<<<<<<<<<<<<<<<<<<"
    )
    logger.info(
        ">>>>>>>>>>>>>>>>> Starting the Data Transformation Pipeline... <<<<<<<<<<<<<<<<<<<<<<<"
    )
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(
        ">>>>>>>>>>>>>>>>> Data Transformation Pipeline completed! <<<<<<<<<<<<<<<<<<<<<<<"
    )
    logger.info(
        ">>>>>>>>>>>>>>>>> Starting the Model Trainer Pipeline... <<<<<<<<<<<<<<<<<<<<<<<"
    )
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(
        ">>>>>>>>>>>>>>>>> Model Trainer Pipeline completed! <<<<<<<<<<<<<<<<<<<<<<<"
    )
    logger.info(
        ">>>>>>>>>>>>>>>>> Starting the Model Evaluation Pipeline... <<<<<<<<<<<<<<<<<<<<<<<"
    )
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.run()
    logger.info(
        ">>>>>>>>>>>>>>>>> Model Evaluation Pipeline completed! <<<<<<<<<<<<<<<<<<<<<<<"
    )
