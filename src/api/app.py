import pandas as pd
import os

from flask import Flask, request, jsonify, render_template

from src.pipeline.stage_11_prediction import PredictionPipeline
from src.api.validator import RequestValidator
from src.utils.logger import logging
from werkzeug.exceptions import HTTPException

# Creates the Flask application.
app = Flask(__name__,template_folder="../templates")

validator = RequestValidator()


REQUIRED_FIELDS = [
    "customerID",
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges"
]


ALLOWED_VALUES = {
    "gender": ["Male", "Female"],
    "Partner": ["Yes", "No"],
    "Dependents": ["Yes", "No"],
    "PhoneService": ["Yes", "No"],
    "MultipleLines": [
        "Yes",
        "No",
        "No phone service"
    ],
    "InternetService": [
        "DSL",
        "Fiber optic",
        "No"
    ],
    "OnlineSecurity": [
        "Yes",
        "No",
        "No internet service"
    ],
    "OnlineBackup": [
        "Yes",
        "No",
        "No internet service"
    ],
    "DeviceProtection": [
        "Yes",
        "No",
        "No internet service"
    ],
    "TechSupport": [
        "Yes",
        "No",
        "No internet service"
    ],
    "StreamingTV": [
        "Yes",
        "No",
        "No internet service"
    ],
    "StreamingMovies": [
        "Yes",
        "No",
        "No internet service"
    ],
    "Contract": [
        "Month-to-month",
        "One year",
        "Two year"
    ],
    "PaperlessBilling": [
        "Yes",
        "No"
    ],
    "PaymentMethod": [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
}


NUMERIC_FIELDS = [
    "tenure",
    "MonthlyCharges"
]


NON_NEGATIVE_FIELDS = [
    "tenure",
    "MonthlyCharges"
]


@app.route("/predict", methods=["POST"])
def predict():

    if request.is_json:

        input_data = request.get_json()

    else:

        input_data = request.form.to_dict()
        try:
            input_data = validator.convert_form_data(
                input_data
            )

        except (TypeError, ValueError):
            return jsonify({
                "error": "Invalid numeric form value"
            }), 400
    # Validate required fields.
    missing_fields = validator.validate_required_fields(
        input_data=input_data,
        required_fields=REQUIRED_FIELDS
    )

    if missing_fields:
        return jsonify({
            "error": "Missing required fields",
            "missing_fields": missing_fields
        }), 400

    # Validate categorical values.
    validation_error = validator.validate_allowed_values(
        input_data=input_data,
        allowed_values=ALLOWED_VALUES
    )

    if validation_error:
        return jsonify({
            "error": (
                f"Invalid value for "
                f"{validation_error['field']}"
            ),
            "allowed_values": (
                validation_error["allowed_values"]
            )
        }), 400

    # Validate SeniorCitizen.
    senior_citizen_error = validator.validate_senior_citizen(
        input_data=input_data
    )

    if senior_citizen_error:
        return jsonify({
            "error": senior_citizen_error
        }), 400

    # Validate numeric fields.
    numeric_error = validator.validate_numeric_fields(
        input_data=input_data,
        numeric_fields=NUMERIC_FIELDS
    )

    if numeric_error:
        return jsonify({
            "error": numeric_error
        }), 400

    # Validate non-negative fields.
    non_negative_error = (
        validator.validate_non_negative_fields(
            input_data=input_data,
            numeric_fields=NON_NEGATIVE_FIELDS
        )
    )

    if non_negative_error:
        return jsonify({
            "error": non_negative_error
        }), 400

    # Validate TotalCharges.
    try:
        float(input_data["TotalCharges"])

    except (TypeError, ValueError):
        return jsonify({
            "error": "TotalCharges must be a numeric value"
        }), 400

    # Convert input dictionary into DataFrame.
    input_data = pd.DataFrame([input_data])

    # Run prediction pipeline.
    pipeline = PredictionPipeline()

    result = pipeline.main(
        input_data=input_data
    )

    if request.is_json:
        return jsonify(result)

    return render_template(
        "index.html",
        result=result
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(Exception)
def handle_exception(error):

    if isinstance(error, HTTPException):
        return jsonify({
            "error": error.description
        }), error.code

    logging.error(
        "Unexpected API error",
        exc_info=True
    )

    return jsonify({
        "error": "Internal server error"
    }), 500

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )