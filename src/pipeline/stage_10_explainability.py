from src.config.configuration import ConfigurationManager
from src.components.explainability import ExplainabilityAnalyzer


class ExplainabilityPipeline:

    def main(self):
        config_manager = ConfigurationManager()

        explainability_config = (
            config_manager.get_explainability_config()
        )

        explainability_analyzer = ExplainabilityAnalyzer(
            config=explainability_config
        )

        explainability_analyzer.initiate_explainability()


if __name__ == "__main__":
    pipeline = ExplainabilityPipeline()
    pipeline.main()