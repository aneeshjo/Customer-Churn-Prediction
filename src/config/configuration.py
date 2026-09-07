from pathlib import Path
from src.constants import (
    CONFIG_FILE_PATH,
      PARAMS_FILE_PATH,
        SCHEMA_FILE_PATH)
import sys

from src.utils.common import read_yaml_file, create_directories
from src.utils.exception import CustomException

from src.entities.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainingConfig,
    ModelEvaluationConfig,
    ModelSelectionConfig,
    ModelTuningConfig,
    ThresholdOptimizationConfig,
    FeatureImportanceConfig,
    ExplainabilityConfig,
    PredictionConfig
)

class ConfigurationManager:
    def __init__(self,
                 config_file_path: Path = CONFIG_FILE_PATH,
                 params_file_path: Path = PARAMS_FILE_PATH,
                 schema_file_path: Path = SCHEMA_FILE_PATH):
        
        self.config = read_yaml_file(config_file_path)
        self.params = read_yaml_file(params_file_path)
        self.schema = read_yaml_file(schema_file_path)

        create_directories(
    [Path(self.config["artifacts_root"])]
)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion_config = self.config["data_ingestion"]
            params=self.params["data_ingestion"]

            create_directories(
        [Path(data_ingestion_config["root_dir"])]
    )


            data_ingestion_config = DataIngestionConfig(
                root_dir=Path(data_ingestion_config["root_dir"]),
                local_data_file=Path(data_ingestion_config["local_data_file"]),
                train_data_file=Path(data_ingestion_config["train_data_file"]),
                test_data_file=Path(data_ingestion_config["test_data_file"]),
                test_size=params["test_size"],
                random_state=params["random_state"],
                target_column=params["target_column"]
            )

            return data_ingestion_config

        except Exception as e:
            raise CustomException(e, sys)

    def get_data_validation_config(self) ->DataValidationConfig:
        try:
            config=self.config["data_validation"]
            schema=self.schema["COLUMNS"]

            create_directories(
                [Path(config["root_dir"])]
            )

            data_validation_config=DataValidationConfig(
                root_dir=Path(config["root_dir"]),
                validation_status_file=Path(config["validation_status_file"]),
                train_data_file=Path(config["train_data_file"]),
                test_data_file=Path(config["test_data_file"]),
                required_columns=schema
            )
            return data_validation_config
        except Exception as e:
            raise CustomException(e,sys)

    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            config=self.config["data_transformation"]
            params=self.params["data_ingestion"]
            create_directories([Path(config["root_dir"])])
            data_transformation_config=DataTransformationConfig(
                root_dir=Path(config["root_dir"]),
                train_data_file=Path(config["train_data_file"]),
                test_data_file=Path(config["test_data_file"]),
                transformed_train_file=Path(config["transformed_train_file"]),
                transformed_test_file=Path(config["transformed_test_file"]),
                target_column=params["target_column"],
                preprocessor_file=Path(config["preprocessor_file"])
            )
            return data_transformation_config
        except Exception as e:
            raise CustomException(e,sys)

    def get_model_training_config(self) -> ModelTrainingConfig:
        try:
            config = self.config["model_training"]
            params=self.params["model_training"]

            create_directories(
                [Path(config["root_dir"])]
            )

            model_training_config = ModelTrainingConfig(
                root_dir=Path(config["root_dir"]),
                train_data_file=Path(config["train_data_file"]),
                test_data_file=Path(config["test_data_file"]),
                model_file=Path(config["model_file"]),
                random_state=params["random_state"],
                n_estimators=params["n_estimators"],
                learning_rate=params["learning_rate"],
                max_depth=params["max_depth"]
            )

            return model_training_config

        except Exception as e:
            raise CustomException(e, sys)

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            config = self.config["model_evaluation"]

            create_directories(
                [Path(config["root_dir"])]
            )

            model_evaluation_config = ModelEvaluationConfig(
                root_dir=Path(config["root_dir"]),
                model_file=Path(config["model_file"]),
                test_data_file=Path(config["test_data_file"]),
                evaluation_file=Path(config["evaluation_file"])
            )

            return model_evaluation_config

        except Exception as e:
            raise CustomException(e, sys)

    def get_model_selection_config(self) -> ModelSelectionConfig:
        try:
            config = self.config["model_selection"]

            create_directories(
                [Path(config["root_dir"])]
            )

            model_selection_config = ModelSelectionConfig(
                root_dir=Path(config["root_dir"]),
                model_file=Path(config["model_file"]),
                evaluation_file=Path(config["evaluation_file"]),
                selected_model_file=Path(config["selected_model_file"]),
                selection_file=Path(config["selection_file"])
            )

            return model_selection_config

        except Exception as e:
            raise CustomException(e, sys)

    def get_model_tuning_config(self) -> ModelTuningConfig:
        try:
            config = self.config["model_tuning"]
            params = self.params["model_tuning"]

            create_directories(
                [Path(config["root_dir"])]
            )

            model_tuning_config = ModelTuningConfig(
                root_dir=Path(config["root_dir"]),
                train_data_file=Path(config["train_data_file"]),
                best_params_file=Path(config["best_params_file"]),
                random_state=params["random_state"],
                cv=params["cv"],
                scoring=params["scoring"],
                n_estimators=params["n_estimators"],
                learning_rate=params["learning_rate"],
                max_depth=params["max_depth"]
            )

            return model_tuning_config

        except Exception as e:
            raise CustomException(e, sys)

    def get_threshold_optimization_config(self) -> ThresholdOptimizationConfig:
        try:
            params = self.params["threshold_optimization"]

            threshold_config = ThresholdOptimizationConfig(
                threshold=params["threshold"]
            )

            return threshold_config

        except Exception as e:
            raise CustomException(e, sys)

    def get_feature_importance_config(self) -> FeatureImportanceConfig:
        try:
            config = self.config["feature_importance"]

            create_directories(
                [Path(config["root_dir"])]
            )

            feature_importance_config = FeatureImportanceConfig(
                root_dir=Path(config["root_dir"]),
                model_file=Path(config["model_file"]),
                preprocessor_file=Path(config["preprocessor_file"]),
                feature_importance_file=Path(
                    config["feature_importance_file"]
                )
            )

            return feature_importance_config

        except Exception as e:
            raise CustomException(e, sys)

                            
    def get_explainability_config(self) -> ExplainabilityConfig:
        try:
            config = self.config["explainability"]

            create_directories(
                [Path(config["root_dir"])]
            )

            explainability_config = ExplainabilityConfig(
                root_dir=Path(config["root_dir"]),
                model_file=Path(config["model_file"]),
                preprocessor_file=Path(
                    config["preprocessor_file"]
                ),
                test_data_file=Path(
                    config["test_data_file"]
                ),
                global_shap_file=Path(
                    config["global_shap_file"]
                ),
                local_shap_file=Path(
                    config["local_shap_file"]
                )
            )

            return explainability_config

        except Exception as e:
            raise CustomException(e, sys)

    def get_prediction_config(self) -> PredictionConfig:
        try:
            config = self.config["prediction"]

            create_directories(
                [Path(config["root_dir"])]
            )

            prediction_config = PredictionConfig(
                root_dir=Path(config["root_dir"]),
                model_file=Path(config["model_file"]),
                preprocessor_file=Path(
                    config["preprocessor_file"]
                )
            )

            return prediction_config

        except Exception as e:
            raise CustomException(e, sys)
