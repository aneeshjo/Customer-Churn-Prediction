from setuptools import setup, find_packages


NAME = "customer_churn_prediction"
VERSION = "0.0.1"
AUTHOR = "ANEESH JOSE"
EMAIL = "aneeshjose012@gmail.com"

HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> list:
    """
    This function is going to return list of requirements
    mention in requirements.txt file
    """
    requirements_list = []
    with open("requirements.txt") as requirement_file:
        requirements_list = requirement_file.readlines()
        requirements_list = [requirement_name.replace("\n", "") for requirement_name in requirements_list]

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)
    return requirements_list


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(),
    install_requires=get_requirements_list()
)