# from src.Chest_cancer import logger
# from Chest_cancer import logger


# logger.info("Welcome to Chest cancer detection")


from Chest_cancer import logger
from Chest_cancer.pipeline.stage_01_Data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e