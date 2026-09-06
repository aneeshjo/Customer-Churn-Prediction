from src.config.configuration import ConfigurationManager
from src.components.model_selection import ModelSelector


class ModelSelectionPipeline:

    def main(self):
        config_manager = ConfigurationManager()

        model_selection_config = (
            config_manager.get_model_selection_config()
        )

        model_selector = ModelSelector(
            config=model_selection_config
        )

        model_selector.initiate_model_selection()


if __name__ == "__main__":
    pipeline = ModelSelectionPipeline()
    pipeline.main()