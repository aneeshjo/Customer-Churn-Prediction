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
    DataValidationConfig
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

