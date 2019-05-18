import numpy as np

from flask import request
from flask_api import status

from application import api, MODEL, FLOWER_SPECIES_NAMES

from application.schemas import PredictRequestSchema, PredictResponseSchema

from application.utils import validate_request_data, validate_response_data


@api.route('/predict', methods=['POST'])
@validate_request_data(PredictRequestSchema)
@validate_response_data(PredictResponseSchema)
def predict():
    # TODO: I know this is running the data through the schema twice b/c validation..
    # TODO: I will work on a cleaner solution later
    flower_data, errs = PredictRequestSchema().load(request.data)

    # since we have some validation checks..
    # it should be totally fine to access the data from the request directly
    single_row_record = np.array(
        [
            flower_data['SepalLength'],
            flower_data['SepalWidth'],
            flower_data['PetalLength'],
            flower_data['PetalWidth'],
            np.power(flower_data['PetalWidth'], 3)
        ]
    ).reshape(1, -1)

    # TODO: what should happen if .predict() takes forever?
    # TODO: or there is are lot more features to consider?
    # TODO: consider a queue approach to let the client take a ticket,
    # TODO: and wait till the processing is done. Flask may not be best for this..
    prediction = MODEL.predict(single_row_record)
    predicted_flower_species = FLOWER_SPECIES_NAMES[prediction]

    return (
        {
            'FlowerID': request.data['FlowerID'],
            'Species': predicted_flower_species[0]
        },
        status.HTTP_200_OK
    )
