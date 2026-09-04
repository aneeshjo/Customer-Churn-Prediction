from pathlib import Path

from src.config.configuration import ConfigurationManager
from src.components.data_transformation import DataTransformation


config_manager = ConfigurationManager()
config = config_manager.get_data_transformation_config()

data_transformation = DataTransformation(config)

(
    X_train_transformed,
    y_train,
    X_test_transformed,
    y_test
) = data_transformation.initiate_data_transformation()


print("\n========== TRANSFORMATION RESULT ==========")

print("X_train shape:", X_train_transformed.shape)
print("y_train shape:", y_train.shape)

print("X_test shape:", X_test_transformed.shape)
print("y_test shape:", y_test.shape)

print("\nUnique y_train values:", y_train.unique())
print("Unique y_test values:", y_test.unique())

print("\nTrain CSV exists:",
      Path(config.transformed_train_file).exists())

print("Test CSV exists:",
      Path(config.transformed_test_file).exists())

print("Preprocessor exists:",
      Path(config.preprocessor_file).exists())