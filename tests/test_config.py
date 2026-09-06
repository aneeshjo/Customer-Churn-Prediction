from pathlib import Path

from src.config.configuration import ConfigurationManager


config_manager = ConfigurationManager()

config = config_manager.get_data_transformation_config()

print("Root directory:", config.root_dir)
print("Train input:", config.train_data_file)
print("Test input:", config.test_data_file)
print("Transformed train:", config.transformed_train_file)
print("Transformed test:", config.transformed_test_file)
print("Preprocessor:", config.preprocessor_file)

# config_manager = ConfigurationManager()

config1 = config_manager.get_model_evaluation_config()

print("Root directory:", config1.root_dir)
print("Model file:", config1.model_file)
print("Test data:", config1.test_data_file)
print("Evaluation file:", config1.evaluation_file)