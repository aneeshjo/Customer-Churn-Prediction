from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation
from src.utils.logger import logging


STAGE_NAME = "Data Validation Stage"


def main():
    try:
        logging.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")

        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(
            config=data_validation_config
        )

        validation_status = data_validation.initiate_data_validation()

        logging.info(
            f"Data validation status: {validation_status}"
        )

        logging.info(
            f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n"
        )

    except Exception as e:
        logging.exception(e)
        raise


if __name__ == "__main__":
    main()