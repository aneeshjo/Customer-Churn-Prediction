import pandas as pd
import sys
import shap

from src.entities.config_entity import ExplainabilityConfig
from src.utils.exception import CustomException
from src.utils.common import load_object
from src.utils.logger import logging


class ExplainabilityAnalyzer:

    def __init__(self, config: ExplainabilityConfig):
        self.config = config

    def load_objects(self):
        try:
            logging.info("Loading selected model")

            model = load_object(
                    self.config.model_file
            )

            logging.info("Selected model loaded successfully")

            logging.info("Loading fitted preprocessor")

            preprocessor = load_object(
                    self.config.preprocessor_file
                )

            logging.info("Fitted preprocessor loaded successfully")

            logging.info("Loading test data")

            test_data = pd.read_csv(
                    self.config.test_data_file
                )

            logging.info(
                    f"Test data loaded successfully: "
                    f"{test_data.shape}"
                )

            return model, preprocessor, test_data

        except Exception as e:
            logging.error(
                    "Failed to load model, preprocessor, or test data"
                )
            raise CustomException(e, sys)

    def prepare_data(self, preprocessor, test_data):
        try:
            logging.info(
                "Preparing transformed test data for SHAP analysis"
            )

            X_test = test_data.drop(
                "Churn",
                axis=1
            )

            feature_names = (
                preprocessor.get_feature_names_out()
            )

            if X_test.shape[1] != len(feature_names):
                raise ValueError(
                    "Number of transformed features does not "
                    "match the preprocessor feature names"
                )

            X_test.columns = feature_names

            logging.info(
                "Transformed test data prepared successfully"
            )

            logging.info(
                f"Transformed test data shape: "
                f"{X_test.shape}"
            )

            return X_test

        except Exception as e:
            logging.error(
                "Failed to prepare transformed test data "
                "for SHAP analysis"
            )
            raise CustomException(e, sys)

    def calculate_shap_values(
        self,
        model,
        X_test_transformed
        ):
        try:
            logging.info("Creating SHAP TreeExplainer")

            explainer = shap.TreeExplainer(model)

            logging.info(
                    "SHAP TreeExplainer created successfully"
                )

            logging.info(
                    "Calculating SHAP values"
                )

            shap_values = explainer.shap_values(
                    X_test_transformed
                )

            logging.info(
                    "SHAP values calculated successfully"
                )

            return shap_values

        except Exception as e:
            logging.error(
                    "Failed to calculate SHAP values"
                )
            raise CustomException(e, sys)

    def prepare_local_shap_values(
        self,
        shap_values,
        feature_names
        ):
        try:
            logging.info(
                    "Preparing local SHAP values"
                )

            local_shap = pd.DataFrame(
                    shap_values,
                    columns=feature_names
                )

            logging.info(
                    "Local SHAP values prepared successfully"
                )

            return local_shap

        except Exception as e:
            logging.error(
                    "Failed to prepare local SHAP values"
                )
            raise CustomException(e, sys)

    def save_global_importance(self, global_importance):
        try:
            logging.info(
                    "Saving global SHAP feature importance"
                )

            global_importance.to_csv(
                    self.config.global_shap_file,
                    index=False
                )

            logging.info(
                    "Global SHAP feature importance saved successfully"
                )

        except Exception as e:
            logging.error(
                    "Failed to save global SHAP feature importance"
                )
            raise CustomException(e, sys)
    def calculate_global_importance(
        self,
        shap_values,
        feature_names
    ):
        try:
            logging.info(
                "Calculating global SHAP feature importance"
            )

            mean_abs_shap = (
                abs(shap_values).mean(axis=0)
            )

            if len(feature_names) != len(mean_abs_shap):
                raise ValueError(
                    "Number of feature names does not match "
                    "number of SHAP importance values"
                )

            global_importance = pd.DataFrame({
                "feature": feature_names,
                "mean_abs_shap": mean_abs_shap
            })

            global_importance = (
                global_importance
                .sort_values(
                    by="mean_abs_shap",
                    ascending=False
                )
                .reset_index(drop=True)
            )

            logging.info(
                "Global SHAP feature importance calculated successfully"
            )

            return global_importance

        except Exception as e:
            logging.error(
                "Failed to calculate global SHAP feature importance"
            )
            raise CustomException(e, sys)

    def save_local_shap_values(self, local_shap):
        try:
            logging.info(
                    "Saving local SHAP values"
                )

            local_shap.to_csv(
                    self.config.local_shap_file,
                    index=False
                )

            logging.info(
                    "Local SHAP values saved successfully"
                )

        except Exception as e:
            logging.error(
                    "Failed to save local SHAP values"
                )
            raise CustomException(e, sys)


    def initiate_explainability(self):
        try:
            logging.info(
                    "Starting explainability analysis"
                )

            model, preprocessor, test_data = (
                    self.load_objects()
                )

            X_test_transformed = self.prepare_data(
                    preprocessor,
                    test_data
                )

            feature_names = (
                    X_test_transformed.columns.tolist()
                )

            shap_values = self.calculate_shap_values(
                    model,
                    X_test_transformed
                )

            global_importance = (
                    self.calculate_global_importance(
                        shap_values,
                        feature_names
                    )
                )

            local_shap = (
                    self.prepare_local_shap_values(
                        shap_values,
                        feature_names
                    )
                )

            self.save_global_importance(
                    global_importance
                )

            self.save_local_shap_values(
                    local_shap
                )

            logging.info(
                    "Explainability analysis completed successfully"
                )

            return global_importance, local_shap

        except Exception as e:
            logging.error(
                    "Explainability analysis failed"
                )
            raise CustomException(e, sys)