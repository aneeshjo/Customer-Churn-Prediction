import pandas as pd

from src.pipeline.stage_11_prediction import PredictionPipeline



def test_prediction_pipeline():

    input_data = pd.DataFrame([{
        "customerID": "TEST002",
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 24,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "Yes",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "One year",
        "PaperlessBilling": "No",
        "PaymentMethod": "Mailed check",
        "MonthlyCharges": 55.0,
        "TotalCharges": "1320.0"
    }])

    pipeline = PredictionPipeline()

    result = pipeline.main(
        input_data=input_data,
    )

    print("\nPrediction Pipeline Result:")
    print(result)

    assert isinstance(result, dict)
    assert result["prediction"] in [0, 1]
    assert result["prediction_label"] in [
        "Churn",
        "No Churn"
    ]
    assert 0 <= result["churn_probability"] <= 1
    assert result["threshold"] == 0.35



if __name__ == "__main__":
    test_prediction_pipeline()
    