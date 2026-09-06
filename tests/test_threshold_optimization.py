from src.components.threshold_optimization import ThresholdOptimizer
from src.config.configuration import ConfigurationManager


def test_threshold_optimization():

    config_manager = ConfigurationManager()

    threshold_config = (
        config_manager.get_threshold_optimization_config()
    )

    optimizer = ThresholdOptimizer(
        config=threshold_config
    )

    probabilities = [0.10, 0.20, 0.34, 0.35, 0.50, 0.80]

    predictions = optimizer.apply_threshold(probabilities)

    print("Threshold:", threshold_config.threshold)
    print("Probabilities:", probabilities)
    print("Predictions:", predictions)

    expected = [0, 0, 0, 1, 1, 1]

    assert predictions.tolist() == expected

test_threshold_optimization()