import sys

import pandas as pd 

from src.entities.config_entity import DataValidationConfig
from src.utils.logger import logging
from src.utils.exception import CustomException

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def validate_columns(self,data:pd.DataFrame)->bool:
        """
        Validates the columns and data types of the given dataframe
        against the expected schema.
        """
        try:
            expected_columns=self.config.required_columns

            # Verify Column Names
            actual_columns=list(data.columns)
            expected_column_names=list(expected_columns.keys())

            if actual_columns != expected_column_names:
                logging.error(
                    "Column names or column order do not match the schema."
                )
                logging.error(
                    f"Expected columns: {expected_column_names}"
                )
                logging.error(
                    f"Actual columns: {actual_columns}"
                )
                return False
             # Check data types
            for column, expected_dtype in expected_columns.items():

                actual_dtype = data[column].dtype

                if expected_dtype == "object":
                    dtype_valid = pd.api.types.is_object_dtype(actual_dtype) or \
                                pd.api.types.is_string_dtype(actual_dtype)

                else:
                    dtype_valid = str(actual_dtype) == expected_dtype

                if not dtype_valid:
                    logging.error(
                        f"Data type mismatch for '{column}'. "
                        f"Expected: {expected_dtype}, "
                        f"Actual: {actual_dtype}"
                    )
                    return False

            logging.info(
                                "Column names and data types validated successfully."
                            )

            return True

        except Exception as e:
            logging.error(
                f"Error during column validation: {e}"
            )
            raise CustomException(e, sys)

    def initiate_data_validation(self):

        try:
            logging.info("Starting data validation process...")

            train_data = pd.read_csv(
                self.config.train_data_file
            )

            test_data = pd.read_csv(
                self.config.test_data_file
            )

            logging.info(
                f"Train data loaded successfully. "
                f"Shape: {train_data.shape}"
            )

            logging.info(
                f"Test data loaded successfully. "
                f"Shape: {test_data.shape}"
            )

            train_valid = self.validate_columns(train_data)
            test_valid = self.validate_columns(test_data)

            validation_status = train_valid and test_valid

            with open(
                self.config.validation_status_file,
                "w"
            ) as status_file:

                status_file.write(
                    f"Validation status: {validation_status}"
                )

            logging.info(
                f"Data validation completed. "
                f"Status: {validation_status}"
            )

            return validation_status

        except Exception as e:
            logging.error(
                f"Error during data validation: {e}"
            )
            raise CustomException(e, sys)

        

        