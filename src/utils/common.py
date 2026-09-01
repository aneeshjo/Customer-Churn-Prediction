import os
import sys
import yaml
import pickle

from pathlib import Path

from src.utils.exception import CustomException
from src.utils.logger import logging


def read_yaml_file(file_path: str) -> dict:
    """
    Reads a YAML file and returns its contents as a dictionary.
    """

    try:
        with open(file_path, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)

        logging.info(f"YAML file {file_path} read successfully")

        return content

    except Exception as e:
        logging.error(f"Error reading YAML file {file_path}: {e}")
        raise CustomException(e, sys)


def save_object(file_path: str, obj: object) -> None:
    """
    Saves a Python object to a file using pickle.
    """

    try:
        directory = os.path.dirname(file_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Object saved to {file_path}")

    except Exception as e:
        logging.error(f"Error saving object to {file_path}: {e}")
        raise CustomException(e, sys)


def load_object(file_path: str) -> object:
    """
    Loads a Python object from a file using pickle.
    """

    try:
        with open(file_path, "rb") as file_obj:
            obj = pickle.load(file_obj)

        logging.info(f"Object loaded from {file_path}")

        return obj

    except Exception as e:
        logging.error(f"Error loading object from {file_path}: {e}")
        raise CustomException(e, sys)


def create_directories(path_to_directories: list) -> None:
    """
    Creates directories if they do not exist.
    """

    try:
        for path in path_to_directories:

            Path(path).mkdir(parents=True, exist_ok=True)

            logging.info(f"Directory created at {path}")

    except Exception as e:
        logging.error(f"Error creating directories: {e}")
        raise CustomException(e, sys)