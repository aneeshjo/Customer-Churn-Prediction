class RequestValidator:

    def validate_required_fields(
        self,
        input_data,
        required_fields
    ):
        missing_fields = [
            field
            for field in required_fields
            if field not in input_data
        ]

        if missing_fields:
            return missing_fields

        return []
    def validate_allowed_values(
    self,
    input_data,
    allowed_values
    ):
        for field, allowed in allowed_values.items():

            if input_data[field] not in allowed:
                return {
                    "field": field,
                    "allowed_values": allowed
                }

        return None
    def validate_senior_citizen(self, input_data):

        if input_data["SeniorCitizen"] not in [0, 1]:
            return "SeniorCitizen must be either 0 or 1"

        return None

    def validate_numeric_fields(
        self,
        input_data,
        numeric_fields
    ):
        for field in numeric_fields:

            if not isinstance(
                input_data[field],
                (int, float)
            ):
                return f"{field} must be a number"

        return None

    def validate_non_negative_fields(
        self,
        input_data,
        numeric_fields
    ):
        for field in numeric_fields:

            if input_data[field] < 0:
                return f"{field} cannot be negative"

        return None

    def convert_form_data(self, input_data):

        input_data = input_data.copy()

        input_data["SeniorCitizen"] = int(
            input_data["SeniorCitizen"]
        )

        input_data["tenure"] = int(
            input_data["tenure"]
        )

        input_data["MonthlyCharges"] = float(
            input_data["MonthlyCharges"]
        )

        return input_data