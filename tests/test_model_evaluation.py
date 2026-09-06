from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluator

config_manager=ConfigurationManager()
config=config_manager.get_model_evaluation_config()

model_evaluator=ModelEvaluator(config=config)


# test_data,model=model_evaluator.load_data()

# X_test,y_test=model_evaluator.prepare_data(test_data)

# print(X_test.shape,y_test.shape)

# y_prediction,y_probability=model_evaluator.generate_predictions(model=model,X_test=X_test)

# print(y_prediction,y_probability)

# metrics=model_evaluator.calculate_metrics(y_test=y_test,y_pred=y_prediction,y_pred_proba=y_probability)

# print(metrics)



def test_model_evaluation():
    config_manager = ConfigurationManager()
    config = config_manager.get_model_evaluation_config()

    evaluator = ModelEvaluator(config)

    metrics = evaluator.initiate_model_evaluation()

    print(metrics)

    assert "accuracy" in metrics
    assert "precision" in metrics
    assert "recall" in metrics
    assert "f1_score" in metrics
    assert "roc_auc" in metrics

test_model_evaluation()


