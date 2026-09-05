# from src.config.configuration import ConfigurationManager
# from src.components.model_training import ModelTrainer


# config_manager = ConfigurationManager()
# config = config_manager.get_model_training_config()

# model_trainer = ModelTrainer(config)

# train_data, test_data = model_trainer.load_data()

# X_train, y_train, X_test, y_test = model_trainer.prepare_data(
#     train_data,
#     test_data
# )
# print("Random state:", config.random_state)
# print("N estimators:", config.n_estimators)
# print("Learning rate:", config.learning_rate)
# print("Max depth:", config.max_depth)
# print("X_train shape:", X_train.shape)
# print("y_train shape:", y_train.shape)
# print("X_test shape:", X_test.shape)
# print("y_test shape:", y_test.shape)

# print("Target values:", y_train.unique())


# model = model_trainer.create_model()

# print("Model:", model)
# print("Number of estimators:", model.n_estimators)
# print("Learning rate:", model.learning_rate)
# print("Max depth:", model.max_depth)
# print("Random state:", model.random_state)



# trained_model = model_trainer.train_model(
#     model,
#     X_train,
#     y_train
# )

# print("Model training completed")
# print("Trained model:", trained_model)

# model_trainer.save_model(trained_model)

# print("Model saved successfully")
# print("Model path:", config.model_file)

from src.config.configuration import ConfigurationManager
from src.components.model_training import ModelTrainer


config_manager = ConfigurationManager()
config = config_manager.get_model_training_config()

model_trainer = ModelTrainer(config)

trained_model = model_trainer.initiate_model_training()

print("Model training pipeline completed successfully")
print("Trained model:", trained_model)
print("Model path:", config.model_file)


from src.utils.common import load_object

loaded_model = load_object(config.model_file)

print("Saved model loaded successfully")
print("Loaded model:", loaded_model)