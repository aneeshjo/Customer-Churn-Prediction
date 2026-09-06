from src.config.configuration import ConfigurationManager
from src.components.model_selection import ModelSelector


def test_model_selection():
    config_manager = ConfigurationManager()

    config = config_manager.get_model_selection_config()

    selector = ModelSelector(config)

    selection = selector.initiate_model_selection()

    print(selection)

    assert selection["selected_model"] == "GradientBoostingClassifier"
    assert selection["selection_metric"] == "roc_auc"
    assert "selection_score" in selection

test_model_selection()