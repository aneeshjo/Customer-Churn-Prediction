from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion


config = ConfigurationManager()

data_ingestion_config = config.get_data_ingestion_config()

data_ingestion = DataIngestion(
    config=data_ingestion_config
)

train_file, test_file = data_ingestion.initiate_data_ingestion()

print("Train file:", train_file)
print("Test file:", test_file)