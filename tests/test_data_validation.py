from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation


config = ConfigurationManager()

data_validation_config = config.get_data_validation_config()

data_validation = DataValidation(
    config=data_validation_config
)

validation_status = data_validation.initiate_data_validation()

print("Validation status:", validation_status)