import pandas as pd
import numpy as np
import sys

from src.entities.config_entity import PredictionConfig
from src.utils.exception import CustomException
from src.utils.common import load_object
from src.utils.logger import logging


class Predictor:

    def __init__(self, config: PredictionConfig):
        self.config = config

    def load_objects(self):
        try:
            logging.info("Loading selected production model")

            model = load_object(
                self.config.model_file
            )

            logging.info(
                "Selected production model loaded successfully"
            )

            logging.info("Loading fitted preprocessor")

            preprocessor = load_object(
                self.config.preprocessor_file
            )

            logging.info(
                "Fitted preprocessor loaded successfully"
            )

            return model, preprocessor

        except Exception as e:
            logging.error(
                "Failed to load model or preprocessor"
            )
            raise CustomException(e, sys)
        
    def prepare_data(self, preprocessor, input_data):
        try:
            logging.info(
                "Preparing input data for prediction"
            )

            input_data = input_data.copy()

            input_data = input_data.drop(
                "customerID",
                axis=1
            )

            input_data["TotalCharges"] = pd.to_numeric(
                input_data["TotalCharges"],
                errors="coerce"
            )

            transformed_data = preprocessor.transform(
                input_data
            )

            

            logging.info(
                "Input data transformed successfully"
            )

            return transformed_data

        except Exception as e:
            logging.error(
                "Failed to prepare input data for prediction"
            )
            raise CustomException(e, sys)
        
    def predict(self, model, transformed_data):
        try:
            logging.info(
                "Generating churn prediction"
            )

            churn_probability = model.predict_proba(
                transformed_data
            )[:, 1]

            logging.info(
                "Churn probability generated successfully"
            )

            return churn_probability

        except Exception as e:
            logging.error(
                "Failed to generate churn prediction"
            )
            raise CustomException(e, sys)

    def apply_threshold(
        self,
        churn_probability,
        threshold
    ):
        try:
            logging.info(
                "Applying prediction threshold"
            )

            prediction = (
                np.array(churn_probability) >= threshold
            ).astype(int)

            logging.info(
                f"Prediction threshold applied: {threshold}"
            )

            return prediction

        except Exception as e:
            logging.error(
                "Failed to apply prediction threshold"
            )
            raise CustomException(e, sys)

    def predict_customer(self, input_data, threshold):
        try:
            logging.info(
                "Starting customer churn prediction"
            )

            model, preprocessor = self.load_objects()

            transformed_data = self.prepare_data(
                preprocessor,
                input_data
            )

            churn_probability = self.predict(
                model,
                transformed_data
            )

            prediction = self.apply_threshold(
                churn_probability,
                threshold
            )

            result = {
                "prediction": int(prediction[0]),
                "prediction_label": (
                    "Churn"
                    if prediction[0] == 1
                    else "No Churn"
                ),
                "churn_probability": float(
                    churn_probability[0]
                ),
                "threshold": threshold
            }

            logging.info(
                "Customer churn prediction completed successfully"
            )

            return result

        except Exception as e:
            logging.error(
                "Customer churn prediction failed"
            )
            raise CustomException(e, sys)