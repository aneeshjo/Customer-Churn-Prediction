import pandas as pd

from src.components.prediction import Predictor
from src.config.configuration import ConfigurationManager


def test_prediction():

    config_manager = ConfigurationManager()

    prediction_config = (
        config_manager.get_prediction_config()
    )

    predictor = Predictor(
        config=prediction_config
    )

    input_data = pd.DataFrame([{
        "customerID": "TEST001",
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 5,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 80.5,
        "TotalCharges": "402.5"
    }])

    result = predictor.predict_customer(
    input_data=input_data,
    threshold=0.35
)

    print("\nPrediction Result:")
    print(result)

    assert isinstance(result, dict)
    assert result["prediction"] in [0, 1]
    assert result["prediction_label"] in [
        "Churn",
        "No Churn"
    ]
    assert 0 <= result["churn_probability"] <= 1
    assert result["threshold"] == 0.35
def test_apply_threshold():

    config_manager = ConfigurationManager()

    prediction_config = (
        config_manager.get_prediction_config()
    )

    predictor = Predictor(
        config=prediction_config
    )

    probabilities = [0.10, 0.34, 0.35, 0.50, 0.80]

    predictions = predictor.apply_threshold(
        churn_probability=probabilities,
        threshold=0.35
    )

    print("\nThreshold Test:")
    print("Probabilities:", probabilities)
    print("Predictions:", predictions)

    assert predictions.tolist() == [0, 0, 1, 1, 1]


if __name__ == "__main__":
    test_prediction()
    test_apply_threshold()