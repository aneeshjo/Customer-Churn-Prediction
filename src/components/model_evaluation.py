import pandas as pd
import sys
import json

from src.utils.exception import CustomException
from src.utils.logger import logging
from src.entities.config_entity import ModelEvaluationConfig

from sklearn.metrics import (
    classification_report,
    accuracy_score,
    precision_score,
    f1_score,
    roc_auc_score,
    recall_score
)

from src.utils.common import load_object


class ModelEvaluator:

    def __init__(self, config:ModelEvaluationConfig):
        self.config = config

    def load_data(self):
        try:
            logging.info("Loading the test dataset")
            test_data=pd.read_csv(self.config.test_data_file)    
            logging.info("Test dataset loaded successfully")

            logging.info("Loading the saved object")
            model=load_object(self.config.model_file)
            logging.info("Model loaded successfully")

            return test_data,model
        except Exception as e:
            logging.error("The data couldn't loaded")
            raise CustomException(e,sys)
        
    def prepare_data(self, test_data):
        try:
            logging.info("Preparing test data")

            X_test = test_data.drop("Churn", axis=1)
            y_test = test_data["Churn"]

            logging.info("Test data prepared successfully")

            return X_test, y_test

        except Exception as e:
            logging.error("Test data preparation failed")
            raise CustomException(e, sys)

    def generate_predictions(self, model, X_test):
        try:
            logging.info("Generating predictions")

            y_pred = model.predict(X_test)
            y_pred_proba = model.predict_proba(X_test)[:, 1]

            logging.info("Predictions generated successfully")

            return y_pred, y_pred_proba

        except Exception as e:
            logging.error("Prediction generation failed")
            raise CustomException(e, sys)


    def calculate_metrics(self, y_test, y_pred, y_pred_proba):
        try:
            logging.info("Calculating evaluation metrics")

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            roc_auc = roc_auc_score(y_test, y_pred_proba)

            metrics = {
                "accuracy": accuracy,
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
                "roc_auc": roc_auc
            }

            logging.info("Evaluation metrics calculated successfully")

            return metrics

        except Exception as e:
            logging.error("Metric calculation failed")
            raise CustomException(e, sys)

    def save_metrics(self, metrics):
        try:
            logging.info("Saving evaluation metrics")

            with open(self.config.evaluation_file, "w") as file:
                json.dump(metrics, file, indent=4)

            logging.info("Evaluation metrics saved successfully")

        except Exception as e:
            logging.error("Failed to save evaluation metrics")
            raise CustomException(e, sys)


    def initiate_model_evaluation(self):
        try:
            logging.info("Starting model evaluation")

            test_data, model = self.load_data()

            X_test, y_test = self.prepare_data(test_data)

            y_pred, y_pred_proba = self.generate_predictions(
                model,
                X_test
            )

            metrics = self.calculate_metrics(
                y_test,
                y_pred,
                y_pred_proba
            )

            self.save_metrics(metrics)

            logging.info("Model evaluation completed successfully")

            return metrics

        except Exception as e:
            logging.error("Model evaluation failed")
            raise CustomException(e, sys)