import yaml
from logging.config import dictConfig

from flask_api import FlaskAPI
from flask import request

from .utils import load_model, load_labels


# Load these at the beginning. If they fail, the rest of the app will also fail.
# TODO: Find a way to dynamically update which model to use without shutting down the app
with open("./../src/ModelConfig.yaml", "r") as f:
    model_config = yaml.safe_load(f)

MODEL = load_model(config=model_config)
FLOWER_SPECIES_NAMES = load_labels(config=model_config)


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s %(process)d] [%(levelname)s] %(message)s',
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


api = FlaskAPI(__name__)


@api.after_request
def log_status_codes_end_endpoints(response):
    status_code = response.status_code

    msg = f'{request.path} - {status_code}'

    if (status_code >= 200) and (status_code < 300):
        api.logger.info(msg)

    elif (status_code >= 300) and (status_code < 400):
        api.logger.debug(msg)

    else:
        api.logger.error(msg)

    return response


# Import these guys at the bottom b/c the whole
# circular import stuff.
import application.views
