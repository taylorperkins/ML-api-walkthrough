from flask import request
from flask_api import status

from application import api

from application.schemas import PredictResponseSchema

from application.utils import validate_response_data

from application.logic.predict import predict as predict_logic


@api.route('/predict', methods=['POST'])
@validate_response_data(PredictResponseSchema)
def predict():
    prediction = predict_logic(**request.data)

    return (
        prediction,
        status.HTTP_200_OK
    )
