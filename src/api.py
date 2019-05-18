import yaml
from logging.config import dictConfig

import numpy as np

from flask_api import FlaskAPI, status
from flask import request

from api_models import PredictRequestSchema, PredictResponseSchema

from utils import (validate_request_data, validate_response_data, load_model, load_labels, log_status_codes_end_endpoints)


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s %(process)d] [%(levelname)s] [%(module)s] %(message)s',
        'datefmt': '%Y-%m-%d %H:%M:%S'
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


application = FlaskAPI(__name__)

MODEL = None
FLOWER_SPECIES_NAMES = None


@application.after_request
def log_status_codes_end_endpoints(response):
    status_code = response.status_code

    msg = f'{request.path} - {status_code}'

    if (status_code >= 200) and (status_code < 300):
        application.logger.info(msg)

    elif (status_code >= 300) and (status_code < 400):
        application.logger.debug(msg)

    else:
        application.logger.error(msg)

    return response


@application.before_first_request
def load_globals():
    # this initial process is just brought over from the sample_prediction.py
    with open("./../src/ModelConfig.yaml", "r") as f:
        model_config = yaml.safe_load(f)

    global MODEL
    global FLOWER_SPECIES_NAMES

    MODEL = load_model(config=model_config)
    FLOWER_SPECIES_NAMES = load_labels(config=model_config)


@application.route('/health')
def health():
    return {'message': 'Success!', 'status_code': 200}, status.HTTP_200_OK


@application.route('/predict', methods=['POST'])
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


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000)
