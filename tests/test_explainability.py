from src.config.configuration import ConfigurationManager
from src.components.explainability import ExplainabilityAnalyzer


def test_explainability():

    config_manager = ConfigurationManager()

    config = config_manager.get_explainability_config()

    analyzer = ExplainabilityAnalyzer(
        config=config
    )

    global_importance, local_shap = (
        analyzer.initiate_explainability()
    )

    print("\nTop 10 SHAP Features:")
    print(global_importance.head(10))

    print(
        "\nGlobal SHAP Shape:",
        global_importance.shape
    )

    print(
        "Local SHAP Shape:",
        local_shap.shape
    )

    print(
        "\nTotal Features:",
        len(global_importance)
    )

    assert len(global_importance) == 45

    assert len(local_shap) == 1409

    assert (
        len(global_importance["feature"])
        ==
        len(global_importance["mean_abs_shap"])
    )

    assert (
        local_shap.shape
        ==
        (1409, 45)
    )


if __name__ == "__main__":
    test_explainability()