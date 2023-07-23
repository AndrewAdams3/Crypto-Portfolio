# exceptions.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
import json

def custom_exception_handler(exc, context):
    # Call the default exception handler to get the standard error response.
    response = exception_handler(exc, context)
    status_code = getattr(exc, 'status_code', 500)

    # If the default handler couldn't handle the exception, create a JSON response.
    if response is None:
        response_data = {
            'error': str(exc),
        }

        response = Response(response_data, status=status_code)  # You can choose an appropriate status code.

    return response
