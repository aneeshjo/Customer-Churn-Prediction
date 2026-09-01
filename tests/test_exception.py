import sys

from src.utils.exception import CustomException


def divide_numbers():

    try:
        result = 10 / 0
        return result

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    divide_numbers()