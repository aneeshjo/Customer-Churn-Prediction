import pandas as pd
import sys

from src.utils.exception import CustomException
from src.utils.logger import logging

from sklearn.ensemble import (
    GradientBoostingClassifier
)
from src.utils.common import save_object
from src.entities.config_entity import ModelTrainingConfig
class ModelTrainer:

    def __init__(self, config:ModelTrainingConfig):
        self.config = config

    def load_data(self):
        try:
            logging.info("Loading the datasets")
            train_data=pd.read_csv(self.config.train_data_file)
            test_data=pd.read_csv(self.config.test_data_file)

            logging.info("Training and test datasets loaded successfully")

            return train_data,test_data
        except Exception as e:
            logging.error("The data couldn't loaded")
            raise CustomException(e,sys)


    def prepare_data(self, train_data, test_data):
        try:
            logging.info("Preparing training and test data")

            X_train = train_data.drop(columns=["Churn"])
            y_train = train_data["Churn"]

            X_test = test_data.drop(columns=["Churn"])
            y_test = test_data["Churn"]

            logging.info("Training and test data prepared successfully")

            return X_train, y_train, X_test, y_test

        except Exception as e:
            logging.error("The training and test data could not be prepared")
            raise CustomException(e, sys)

    def create_model(self):
        try:
            logging.info("Creating Gradient Boosting model")

            model = GradientBoostingClassifier(
                n_estimators=self.config.n_estimators,
                learning_rate=self.config.learning_rate,
                max_depth=self.config.max_depth,
                random_state=self.config.random_state
            )

            logging.info("Gradient Boosting model created successfully")

            return model

        except Exception as e:
            logging.error("Gradient Boosting model could not be created")
            raise CustomException(e, sys)

    def train_model(self, model, X_train, y_train):
        try:
            logging.info("Training Gradient Boosting model")

            model.fit(X_train, y_train)

            logging.info("Gradient Boosting model trained successfully")

            return model

        except Exception as e:
            logging.error("Gradient Boosting model could not be trained")
            raise CustomException(e, sys)

    def save_model(self, model):
        try:
            logging.info("Saving trained Gradient Boosting model")

            save_object(
                file_path=self.config.model_file,
                obj=model
            )

            logging.info(
                f"Gradient Boosting model saved successfully at "
                f"{self.config.model_file}"
            )

        except Exception as e:
            logging.error("The trained model could not be saved")
            raise CustomException(e, sys)


    def initiate_model_training(self):
        try:
            logging.info("Starting model training stage")

            train_data, test_data = self.load_data()

            X_train, y_train, X_test, y_test = self.prepare_data(
                train_data,
                test_data
            )

            model = self.create_model()

            trained_model = self.train_model(
                model,
                X_train,
                y_train
            )

            self.save_model(trained_model)

            logging.info("Model training stage completed successfully")

            return trained_model

        except Exception as e:
            logging.error("Model training stage failed")
            raise CustomException(e, sys)