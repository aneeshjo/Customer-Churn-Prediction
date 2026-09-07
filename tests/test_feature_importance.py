from src.config.configuration import ConfigurationManager
from src.components.feature_importance import FeatureImportanceAnalyzer


def test_feature_importance():

    config_manager = ConfigurationManager()

    config = config_manager.get_feature_importance_config()

    analyzer = FeatureImportanceAnalyzer(
        config=config
    )

    feature_importance = (
        analyzer.initiate_feature_importance()
    )

    print("\nTop 10 Important Features:")
    print(feature_importance.head(10))

    print(
        "\nTotal Features:",
        len(feature_importance)
    )

    print(
        "Total Importance:",
        feature_importance["importance"].sum()
    )

    assert len(feature_importance) > 0

    assert (
        len(feature_importance["feature"])
        ==
        len(feature_importance["importance"])
    )

    assert abs(
        feature_importance["importance"].sum() - 1.0
    ) < 1e-6



if __name__ == "__main__":
    test_feature_importance()