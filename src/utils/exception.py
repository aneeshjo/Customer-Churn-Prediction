from email import message
import sys

class CustomException(Exception):
    def __init__(self, error_message: str, error_detail: sys):
        super().__init__(message)
        self.error_message=self.get_detailed_error_message(
            error_message=error_message,
              error_detail=error_detail
              )

    @staticmethod
    def get_detailed_error_message(error_message: str, error_detail: sys) -> str:
        """
        error_message: str: Exception message
        error_detail: sys: Object of sys module
        """
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        detailed_error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return detailed_error_message

    def __str__(self) -> str:
        return self.error_message