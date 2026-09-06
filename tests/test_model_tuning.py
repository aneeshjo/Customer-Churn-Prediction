from src.config.configuration import ConfigurationManager
from src.components.model_tuning import ModelTuner


def test_model_tuning():
    config_manager = ConfigurationManager()

    config = config_manager.get_model_tuning_config()

    tuner = ModelTuner(config)

    best_params, best_score = tuner.initiate_model_tuning()

    print("Best Parameters:", best_params)
    print("Best ROC-AUC:", best_score)

    assert isinstance(best_params, dict)
    assert "n_estimators" in best_params
    assert "learning_rate" in best_params
    assert "max_depth" in best_params
    assert best_score > 0

test_model_tuning()