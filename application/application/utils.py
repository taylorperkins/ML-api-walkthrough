import os

from functools import wraps

from sklearn.externals import joblib

import numpy as np

from flask import request
from flask_api import status


def validate_request_data(schema):
    """Try to validate request data given a schema
    If there is an err, raise 400 with validation message
    Else, run the endpoint like normal
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):

            # validate the data coming in from the client
            errors = schema().validate(request.data)

            if errors:
                return errors, status.HTTP_400_BAD_REQUEST

            return f(*args, **kwargs)

        return wrapper
    return decorator


def validate_response_data(schema):
    """Try to validate response data given a schema
    If there is an err, raise 500 with validation message
    Else, return the endpoint like normal
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # make initial request, catching the response
            response_data, status_code = f(*args, **kwargs)

            # validate the response
            errors = schema().validate(response_data)

            if errors:
                return errors, status.HTTP_500_INTERNAL_SERVER_ERROR

            return response_data, status_code

        return wrapper
    return decorator


def load_model(config):
    """Helper function to hold all info regarding loading in the model"""
    model_objects_folder = config["Model"]["Objects"]["FolderName"]
    pickeled_model_file_name = config["Model"]["Objects"]["ModelFileName"]

    model_location = os.path.join(model_objects_folder, pickeled_model_file_name)

    # Load the model from the file
    return joblib.load(model_location)


def load_labels(config):
    """Helper function to hold all info regarding loading in the labels"""
    model_objects_folder = config["Model"]["Objects"]["FolderName"]
    target_class_names_file_name = config["Model"]["Objects"][
        "TargetClassLabelNamesFileName"
    ]

    flower_class_names_location = os.path.join(
        model_objects_folder, target_class_names_file_name
    )

    return np.load(flower_class_names_location)
