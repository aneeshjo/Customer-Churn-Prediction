import pandas as pd
import sys
import json

from sklearn.ensemble import GradientBoostingClassifier

from src.utils.exception import CustomException
from src.utils.logger import logging
from src.entities.config_entity import ModelTuningConfig

from sklearn.model_selection import GridSearchCV


class ModelTuner:

    def __init__(self, config: ModelTuningConfig):
        self.config = config


    def load_data(self):
        try:
            logging.info("Loading training data for hyperparameter tuning")

            train_data = pd.read_csv(self.config.train_data_file)

            logging.info("Training data loaded successfully")

            return train_data

        except Exception as e:
            logging.error("Failed to load training data")
            raise CustomException(e, sys)

    def prepare_data(self, train_data):
        try:
            logging.info("Preparing training data for hyperparameter tuning")

            X_train = train_data.drop("Churn", axis=1)
            y_train = train_data["Churn"]

            logging.info("Training data prepared successfully")

            return X_train, y_train

        except Exception as e:
            logging.error("Training data preparation failed")
            raise CustomException(e, sys)
    def create_model(self, params):
        try:
            logging.info("Creating Gradient Boosting model")

            model = GradientBoostingClassifier(
                n_estimators=params["n_estimators"],
                learning_rate=params["learning_rate"],
                max_depth=params["max_depth"],
                random_state=self.config.random_state
            )

            logging.info("Gradient Boosting model created successfully")

            return model

        except Exception as e:
            logging.error("Failed to create Gradient Boosting model")
            raise CustomException(e, sys)

    def tune_model(self, X_train, y_train):
        try:
            logging.info("Starting hyperparameter tuning")

            model = GradientBoostingClassifier(
                random_state=self.config.random_state
            )

            param_grid = {
                "n_estimators": self.config.n_estimators,
                "learning_rate": self.config.learning_rate,
                "max_depth": self.config.max_depth
            }

            grid_search = GridSearchCV(
                estimator=model,
                param_grid=param_grid,
                cv=self.config.cv,
                scoring=self.config.scoring,
                n_jobs=-1
            )

            grid_search.fit(X_train, y_train)

            logging.info("Hyperparameter tuning completed successfully")

            return grid_search.best_params_, grid_search.best_score_

        except Exception as e:
            logging.error("Hyperparameter tuning failed")
            raise CustomException(e, sys)

    def save_best_params(self, best_params, best_score):
        try:
            logging.info("Saving best hyperparameters")

            tuning_results = {
                "best_params": best_params,
                "best_score": best_score
            }

            with open(self.config.best_params_file, "w") as file:
                json.dump(tuning_results, file, indent=4)

            logging.info("Best hyperparameters saved successfully")

        except Exception as e:
            logging.error("Failed to save best hyperparameters")
            raise CustomException(e, sys)

    def initiate_model_tuning(self):
        try:
            logging.info("Starting hyperparameter tuning")

            train_data = self.load_data()

            X_train, y_train = self.prepare_data(train_data)

            best_params, best_score = self.tune_model(
                X_train,
                y_train
            )

            self.save_best_params(
                best_params,
                best_score
            )

            logging.info("Hyperparameter tuning completed successfully")

            return best_params, best_score

        except Exception as e:
            logging.error("Hyperparameter tuning failed")
            raise CustomException(e, sys)