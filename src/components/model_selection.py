import json
import sys
import logging
import shutil

from src.utils.exception import CustomException
from src.entities.config_entity import ModelSelectionConfig


class ModelSelector:

    def __init__(self, config: ModelSelectionConfig):
        self.config = config

    def load_evaluation(self):
        try:
            logging.info("Loading model evaluation results")

            with open(self.config.evaluation_file, "r") as file:
                metrics = json.load(file)

            logging.info("Model evaluation results loaded successfully")

            return metrics

        except Exception as e:
            logging.error("Failed to load model evaluation results")
            raise CustomException(e, sys)

    def select_model(self, metrics):
        try:
            logging.info("Selecting the production model")

            selected_model = "GradientBoostingClassifier"

            selection = {
                "selected_model": selected_model,
                "selection_metric": "roc_auc",
                "selection_score": metrics["roc_auc"]
            }

            logging.info(
                f"Production model selected: {selected_model}"
            )

            return selection

        except Exception as e:
            logging.error("Model selection failed")
            raise CustomException(e, sys)

    def save_selection(self, selection):
        try:
            logging.info("Saving model selection results")

            with open(self.config.selection_file, "w") as file:
                json.dump(selection, file, indent=4)

            logging.info("Model selection results saved successfully")

        except Exception as e:
            logging.error("Failed to save model selection results")
            raise CustomException(e, sys)

    def save_selected_model(self):
        try:
            logging.info("Saving selected production model")

            shutil.copy2(
                self.config.model_file,
                self.config.selected_model_file
            )

            logging.info("Selected production model saved successfully")

        except Exception as e:
            logging.error("Failed to save selected production model")
            raise CustomException(e, sys)

    def initiate_model_selection(self):
        try:
            logging.info("Starting model selection")

            metrics = self.load_evaluation()

            selection = self.select_model(metrics)

            self.save_selection(selection)

            self.save_selected_model()

            logging.info("Model selection completed successfully")

            return selection

        except Exception as e:
            logging.error("Model selection failed")
            raise CustomException(e, sys)