import sys
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.entities.config_entity import DataIngestionConfig
from src.utils.exception import CustomException
from src.utils.logger import logging

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion process...")
        try:
            #Read the raw data
            data = pd.read_csv(self.config.local_data_file)
            logging.info("Raw data read successfully.")

            logging.info(
                f"Raw dataset loaded successfully. "
                f"Shape: {data.shape}"
            )

            #train test split
            train_set, test_set = train_test_split(data, 
                             test_size=self.config.test_size, 
                            random_state=self.config.random_state,
                            stratify=data[self.config.target_column])
            logging.info(
                f"Train and test data split successfully. "
                f"Train shape: {train_set.shape}, Test shape: {test_set.shape}"
            )

            #Save the train and test data
            train_set.to_csv(self.config.train_data_file, index=False)
            test_set.to_csv(self.config.test_data_file, index=False)

            logging.info(
                f"Train and test data saved successfully. "
                f"Train file: {self.config.train_data_file}, Test file: {self.config.test_data_file}"
            )

            return self.config.train_data_file, self.config.test_data_file
        except Exception as e:
            logging.error(f"Error during data ingestion: {e}")
            raise CustomException(e, sys)
