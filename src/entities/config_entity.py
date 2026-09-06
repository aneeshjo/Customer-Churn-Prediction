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


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir : Path
    train_data_file: Path
    test_data_file: Path
    model_file: Path
    random_state: int
    n_estimators: int
    learning_rate: float
    max_depth: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_file: Path
    test_data_file: Path
    evaluation_file: Path

@dataclass(frozen=True)
class ModelSelectionConfig:
    root_dir: Path
    model_file: Path
    evaluation_file: Path
    selected_model_file: Path
    selection_file: Path

@dataclass(frozen=True)
class ModelTuningConfig:
    root_dir: Path
    train_data_file: Path
    best_params_file: Path
    random_state: int
    cv: int
    scoring: str
    n_estimators: list
    learning_rate: list
    max_depth: list


@dataclass(frozen=True)
class ThresholdOptimizationConfig:
    threshold: float