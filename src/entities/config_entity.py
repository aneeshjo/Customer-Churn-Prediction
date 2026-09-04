from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path
    train_data_file: Path
    test_data_file: Path
    test_size: float 
    random_state: int
    target_column: str

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir:Path
    validation_status_file:Path
    train_data_file : Path
    test_data_file : Path
    required_columns:dict
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_data_file: Path
    test_data_file : Path
    transformed_train_file:Path
    transformed_test_file :Path
    target_column :str
    preprocessor_file : Path