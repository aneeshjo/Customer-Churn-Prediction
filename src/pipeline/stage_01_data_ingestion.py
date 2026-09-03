from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.utils.logger import logging
from src.utils.exception import CustomException
import sys

STAGE_NAME = "Data Ingestion Stage"

def main():
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        config = ConfigurationManager()

        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(
            config=data_ingestion_config
        )

        train_file, test_file = data_ingestion.initiate_data_ingestion()

        logging.info(f"Train file: {train_file}")
        logging.info(f"Test file: {test_file}")

        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()