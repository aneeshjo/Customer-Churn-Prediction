from src.config.configuration import ConfigurationManager
from src.components.model_training import ModelTrainer


class ModelTrainingPipeline:

    def main(self):
        config_manager = ConfigurationManager()

        model_training_config = (
            config_manager.get_model_training_config()
        )

        model_trainer = ModelTrainer(
            config=model_training_config
        )

        model_trainer.initiate_model_training()


if __name__ == "__main__":
    pipeline = ModelTrainingPipeline()
    pipeline.main()