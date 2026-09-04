import sys

from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.utils.exception import CustomException
from src.utils.logger import logging


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            config = config_manager.get_data_transformation_config()

            data_transformation = DataTransformation(config)

            data_transformation.initiate_data_transformation()

            logging.info(
                "Data transformation stage completed successfully."
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        logging.info(
            "Stage 03 Data Transformation started."
        )

        obj = DataTransformationTrainingPipeline()
        obj.main()

        logging.info(
            "Stage 03 Data Transformation completed."
        )

    except Exception as e:
        raise CustomException(e, sys)