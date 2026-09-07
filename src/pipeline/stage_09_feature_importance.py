from src.config.configuration import ConfigurationManager
from src.components.feature_importance import FeatureImportanceAnalyzer


class FeatureImportancePipeline:

    def main(self):
        config_manager = ConfigurationManager()

        feature_importance_config = (
            config_manager.get_feature_importance_config()
        )

        feature_importance_analyzer = FeatureImportanceAnalyzer(
            config=feature_importance_config
        )

        feature_importance_analyzer.initiate_feature_importance()


if __name__ == "__main__":
    pipeline = FeatureImportancePipeline()
    pipeline.main()