from src.config.configuration import ConfigurationManager


def test_prediction_config():

    config_manager = ConfigurationManager()

    config = config_manager.get_prediction_config()

    print("\nPrediction Configuration:")
    print("Root Directory:", config.root_dir)
    print("Model File:", config.model_file)
    print("Preprocessor File:", config.preprocessor_file)

    assert config.root_dir.exists()
    assert config.model_file.exists()
    assert config.preprocessor_file.exists()


if __name__ == "__main__":
    test_prediction_config()