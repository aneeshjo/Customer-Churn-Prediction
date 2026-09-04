from pathlib import Path
import sys

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from src.utils.exception import CustomException
from src.utils.logger import logging
from src.utils.common import save_object
from src.entities.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        try:
            self.config=config
        except Exception as e:
            raise CustomException(e,sys)

    def load_data(self):
        try:
            train_data=pd.read_csv(self.config.train_data_file)
            test_data=pd.read_csv(self.config.test_data_file)
            logging.info("Train and test data loaded successfully")

            return train_data,test_data
        except Exception as e:
            raise CustomException(e,sys)

    def prepare_data(self, train_data, test_data):
        try:
            # Separate target from features
            X_train=train_data.drop(columns=[self.config.target_column])
            y_train=train_data[self.config.target_column]

            X_test=test_data.drop(columns=[self.config.target_column])
            y_test=test_data[self.config.target_column]
            # Remove customer identifier
            X_train = X_train.drop(columns=["customerID"])
            X_test = X_test.drop(columns=["customerID"])

            logging.info("Target separated and customerID removed.")

            return X_train, y_train, X_test, y_test

        except Exception as e:
            raise CustomException(e, sys)
    def convert_total_charges(self, X_train, X_test):
        try:
            X_train = X_train.copy()
            X_test = X_test.copy()

            X_train["TotalCharges"] = pd.to_numeric(
                X_train["TotalCharges"],
                errors="coerce"
            )

            X_test["TotalCharges"] = pd.to_numeric(
                X_test["TotalCharges"],
                errors="coerce"
            )

            logging.info("TotalCharges converted to numeric.")

            return X_train, X_test

        except Exception as e:
            raise CustomException(e, sys)

    def get_feature_columns(self, X_train):
        try:
            numerical_columns = X_train.select_dtypes(
                include=["int64", "float64"]
            ).columns.tolist()

            categorical_columns = X_train.select_dtypes(
                include=["object"]
            ).columns.tolist()

            logging.info(
                f"Numerical columns: {numerical_columns}"
            )
            logging.info(
                f"Categorical columns: {categorical_columns}"
            )

            return numerical_columns, categorical_columns

        except Exception as e:
            raise CustomException(e, sys)

    def create_numerical_pipeline(self):
        try:
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            logging.info("Numerical preprocessing pipeline created.")

            return numerical_pipeline

        except Exception as e:
            raise CustomException(e, sys)

    def create_categorical_pipeline(self):
        try:
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "encoder",
                        OneHotEncoder(
                            handle_unknown="ignore",
                            sparse_output=False
                        )
                    )
                ]
            )

            logging.info("Categorical preprocessing pipeline created.")

            return categorical_pipeline

        except Exception as e:
            raise CustomException(e, sys)
        
    def create_preprocessor(
        self,
        numerical_columns,
        categorical_columns
    ):
        try:
            numerical_pipeline = self.create_numerical_pipeline()
            categorical_pipeline = self.create_categorical_pipeline()

            preprocessor = ColumnTransformer(
                transformers=[
                    (
                        "numerical",
                        numerical_pipeline,
                        numerical_columns
                    ),
                    (
                        "categorical",
                        categorical_pipeline,
                        categorical_columns
                    )
                ]
            )

            logging.info("Preprocessor created successfully.")

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def transform_data(
    self,
    preprocessor,
    X_train,
    X_test
    ):
        try:
            X_train_transformed = preprocessor.fit_transform(X_train)
            X_test_transformed = preprocessor.transform(X_test)

            logging.info(
                "Training and test data transformed successfully."
            )

            return X_train_transformed, X_test_transformed

        except Exception as e:
            raise CustomException(e, sys)

    def encode_target(self, y_train, y_test):
        try:
            y_train = y_train.map({"Yes": 1, "No": 0})
            y_test = y_test.map({"Yes": 1, "No": 0})

            logging.info("Target variable encoded successfully.")

            return y_train, y_test

        except Exception as e:
            raise CustomException(e, sys)

    def save_transformed_data(
    self,
    X_train_transformed,
    y_train,
    X_test_transformed,
    y_test
    ):
        try:
            train_data = pd.DataFrame(X_train_transformed)
            train_data[self.config.target_column] = y_train.to_numpy()

            test_data = pd.DataFrame(X_test_transformed)
            test_data[self.config.target_column] = y_test.to_numpy()

            train_data.to_csv(
                self.config.transformed_train_file,
                index=False
            )

            test_data.to_csv(
                self.config.transformed_test_file,
                index=False
            )

            logging.info(
                "Transformed train and test data saved successfully."
            )

        except Exception as e:
            raise CustomException(e, sys)

    def save_preprocessor(self, preprocessor):
        try:
            save_object(
                file_path=self.config.preprocessor_file,
                obj=preprocessor
            )

            logging.info(
                "Preprocessor saved successfully."
            )

        except Exception as e:
            raise CustomException(e, sys)


    def initiate_data_transformation(self):
        try:
            # 1. Load data
            train_data, test_data = self.load_data()

            # 2. Separate target and remove customerID
            X_train, y_train, X_test, y_test = self.prepare_data(
                train_data,
                test_data
            )

            # 3. Convert TotalCharges to numeric
            X_train, X_test = self.convert_total_charges(
                X_train,
                X_test
            )

            # 4. Identify numerical and categorical columns
            numerical_columns, categorical_columns = (
                self.get_feature_columns(X_train)
            )

            # 5. Create preprocessor
            preprocessor = self.create_preprocessor(
                numerical_columns,
                categorical_columns
            )

            # 6. Transform features
            X_train_transformed, X_test_transformed = (
                self.transform_data(
                    preprocessor,
                    X_train,
                    X_test
                )
            )

            # 7. Encode target
            y_train, y_test = self.encode_target(
                y_train,
                y_test
            )

            # 8. Save transformed datasets
            self.save_transformed_data(
                X_train_transformed,
                y_train,
                X_test_transformed,
                y_test
            )

            # 9. Save fitted preprocessor
            self.save_preprocessor(preprocessor)

            logging.info("Data transformation completed successfully.")

            return (
                X_train_transformed,
                y_train,
                X_test_transformed,
                y_test
            )

        except Exception as e:
            raise CustomException(e, sys)

