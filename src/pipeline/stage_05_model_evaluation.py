from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluator


class ModelEvaluationPipeline:

    def main(self):
        config_manager = ConfigurationManager()

        model_evaluation_config = (
            config_manager.get_model_evaluation_config()
        )

        model_evaluator = ModelEvaluator(
            config=model_evaluation_config
        )

        model_evaluator.initiate_model_evaluation()


if __name__ == "__main__":
    pipeline = ModelEvaluationPipeline()
    pipeline.main()