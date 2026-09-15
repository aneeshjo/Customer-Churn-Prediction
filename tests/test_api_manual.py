import requests


URL = "http://127.0.0.1:5000/predict"


VALID_CUSTOMER = {
    "customerID": "TEST-001",
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.5,
    "TotalCharges": "846.0"
}


TEST_CASES = {

    "1. Valid customer": VALID_CUSTOMER,

    "2. Missing fields": {
        "customerID": "TEST-002",
        "gender": "Female",
        "tenure": 12,
        "MonthlyCharges": 70.5
    },

    "3. Invalid gender": {
        **VALID_CUSTOMER,
        "gender": "Unknown"
    },

    "4. Invalid SeniorCitizen": {
        **VALID_CUSTOMER,
        "SeniorCitizen": 5
    },

    "5. Tenure wrong type": {
        **VALID_CUSTOMER,
        "tenure": "12"
    },

    "6. Negative tenure": {
        **VALID_CUSTOMER,
        "tenure": -5
    },

    "7. Invalid Partner": {
        **VALID_CUSTOMER,
        "Partner": "Maybe"
    },

    "8. MonthlyCharges wrong type": {
        **VALID_CUSTOMER,
        "MonthlyCharges": "hello"
    },

    "9. Invalid TotalCharges": {
        **VALID_CUSTOMER,
        "TotalCharges": "hello"
    }
}


for test_name, data in TEST_CASES.items():

    print("\n" + "=" * 60)
    print(test_name)
    print("=" * 60)

    response = requests.post(
        URL,
        json=data
    )

    print("Status:", response.status_code)
    print("Response:")

    try:
        print(response.json())
    except ValueError:
        print(response.text)