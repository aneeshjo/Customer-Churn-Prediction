from src.config.configuration import ConfigurationManager
from src.components.prediction import Predictor


class PredictionPipeline:

    def main(self, input_data):

        config_manager = ConfigurationManager()

        prediction_config = (
            config_manager.get_prediction_config()
        )

        threshold_config = (
            config_manager.get_threshold_optimization_config()
        )

        predictor = Predictor(
            config=prediction_config
        )

        result = predictor.predict_customer(
            input_data=input_data,
            threshold=threshold_config.threshold
        )

        return result