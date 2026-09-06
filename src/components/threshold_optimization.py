import sys
import numpy as np

from src.entities.config_entity import ThresholdOptimizationConfig
from src.utils.exception import CustomException
from src.utils.logger import logging


class ThresholdOptimizer:

    def __init__(self, config: ThresholdOptimizationConfig):
        self.config = config

    def apply_threshold(self, y_pred_proba):
        try:
            logging.info("Applying classification threshold")

            y_pred = (
                np.array(y_pred_proba) >= self.config.threshold
            ).astype(int)

            logging.info(
                f"Classification threshold applied: "
                f"{self.config.threshold}"
            )

            return y_pred

        except Exception as e:
            logging.error("Failed to apply classification threshold")
            raise CustomException(e, sys)