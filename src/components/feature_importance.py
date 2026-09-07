import pandas as pd
import sys

from src.entities.config_entity import FeatureImportanceConfig
from src.utils.exception import CustomException
from src.utils.common import load_object
from src.utils.logger import logging


class FeatureImportanceAnalyzer:

    def __init__(self, config: FeatureImportanceConfig):
        self.config = config

    def load_objects(self):
        try:
            logging.info("Loading selected model")
            model = load_object(self.config.model_file)

            logging.info("Selected model loaded successfully")

            logging.info("Loading fitted preprocessor")
            preprocessor = load_object(
                self.config.preprocessor_file
            )

            logging.info("Fitted preprocessor loaded successfully")

            return model, preprocessor

        except Exception as e:
            logging.error("Failed to load model or preprocessor")
            raise CustomException(e, sys)

    def get_feature_names(self, preprocessor):
        try:
            logging.info("Extracting transformed feature names")

            feature_names = preprocessor.get_feature_names_out()

            logging.info(
                f"Extracted {len(feature_names)} feature names"
            )

            return feature_names

        except Exception as e:
            logging.error("Failed to extract feature names")
            raise CustomException(e, sys)

    def calculate_feature_importance(
        self,
        model,
        feature_names
    ):
        try:
            logging.info("Calculating feature importance")

            importances = model.feature_importances_

            if len(feature_names) != len(importances):
                raise ValueError(
                    "Number of feature names does not match "
                    "number of feature importance values"
                )

            feature_importance = pd.DataFrame({
                "feature": feature_names,
                "importance": importances
            })

            feature_importance = feature_importance.sort_values(
                by="importance",
                ascending=False
            ).reset_index(drop=True)

            logging.info(
                "Feature importance calculated successfully"
            )

            return feature_importance

        except Exception as e:
            logging.error("Failed to calculate feature importance")
            raise CustomException(e, sys)

    def save_feature_importance(self, feature_importance):
        try:
            logging.info("Saving feature importance")

            feature_importance.to_csv(
                self.config.feature_importance_file,
                index=False
            )

            logging.info(
                "Feature importance saved successfully"
            )

        except Exception as e:
            logging.error("Failed to save feature importance")
            raise CustomException(e, sys)

    def initiate_feature_importance(self):
        try:
            logging.info("Starting feature importance analysis")

            model, preprocessor = self.load_objects()

            feature_names = self.get_feature_names(
                preprocessor
            )

            feature_importance = (
                self.calculate_feature_importance(
                    model,
                    feature_names
                )
            )

            self.save_feature_importance(
                feature_importance
            )

            logging.info(
                "Feature importance analysis completed successfully"
            )

            return feature_importance

        except Exception as e:
            logging.error(
                "Feature importance analysis failed"
            )
            raise CustomException(e, sys)