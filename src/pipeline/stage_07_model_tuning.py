from src.config.configuration import ConfigurationManager
from src.components.model_tuning import ModelTuner


class ModelTuningPipeline:

    def main(self):
        config_manager = ConfigurationManager()

        model_tuning_config = (
            config_manager.get_model_tuning_config()
        )

        model_tuner = ModelTuner(
            config=model_tuning_config
        )

        model_tuner.initiate_model_tuning()


if __name__ == "__main__":
    pipeline = ModelTuningPipeline()
    pipeline.main()