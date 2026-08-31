import os
from pathlib import Path


project_name = "Customer Churn Prediction"


list_of_files = [

    # Project configuration
    "config/config.yaml",
    "config/params.yaml",
    "config/schema.yaml",

    # Source package
    "src/__init__.py",

    # Components
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_validation.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",

    # Pipeline
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",

    # Utilities
    "src/utils/__init__.py",
    "src/utils/logger.py",
    "src/utils/exception.py",

    "notebook/01_EDA.ipynb",

    # Flask
    "templates/index.html",
    "static/css/style.css",

    # Application
    "app.py",
    "main.py",

    # Requirements
    "requirements.txt",

    # Documentation
    "README.md",

]


for file_path in list_of_files:

    file_path = Path(file_path)

    file_directory = file_path.parent

    if file_directory != Path(""):
        os.makedirs(file_directory, exist_ok=True)

    if not file_path.exists():
        file_path.touch()

        print(f"Created: {file_path}")

    else:
        print(f"Already exists: {file_path}")