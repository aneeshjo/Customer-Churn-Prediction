from src.config.configuration import ConfigurationManager


def test_explainability_config():

    config_manager = ConfigurationManager()

    config = config_manager.get_explainability_config()

    print("\nExplainability Configuration:")
    print("Root Directory:", config.root_dir)
    print("Model File:", config.model_file)
    print("Preprocessor File:", config.preprocessor_file)
    print("Test Data File:", config.test_data_file)
    print("Global SHAP File:", config.global_shap_file)
    print("Local SHAP File:", config.local_shap_file)

    assert config.root_dir.exists()
    assert config.model_file.exists()
    assert config.preprocessor_file.exists()
    assert config.test_data_file.exists()

if __name__=="__main__":
    test_explainability_config()