from src.config.configuration import ConfigurationManager
from src.components.threshold_optimization import ThresholdOptimizer


class ThresholdOptimizationPipeline:

    def main(self):
        config_manager = ConfigurationManager()

        threshold_config = (
            config_manager.get_threshold_optimization_config()
        )

        threshold_optimizer = ThresholdOptimizer(
            config=threshold_config
        )

        # Temporary validation of the configured threshold
        probabilities = [0.10, 0.20, 0.34, 0.35, 0.50, 0.80]

        predictions = threshold_optimizer.apply_threshold(
            probabilities
        )

        print("Threshold:", threshold_config.threshold)
        print("Predictions:", predictions)


if __name__ == "__main__":
    pipeline = ThresholdOptimizationPipeline()
    pipeline.main()