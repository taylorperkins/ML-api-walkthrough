import yaml
import os

import numpy as np

from sklearn.externals import joblib

from flask_api import FlaskAPI, status


app = FlaskAPI(__name__)


@app.route('/health')
def health():
    return 'Healthcheck says go!', status.HTTP_200_OK


@app.route('/predict', methods=['POST'])
def predict():
    # TODO: actually implement the dynamic prediction from the request.
    # TODO: Just bringing this over from the sample_prediction.py for now.
    sepal_length = 1.0
    sepal_width = 1.6
    petal_length = 1.1
    petal_width = 1.5
    petal_width_cubed = np.power(petal_width, 3)

    single_row_record = np.array(
        [sepal_length, sepal_width, petal_length, petal_width, petal_width_cubed]
    ).reshape(1, -1)

    prediction = MODEL.predict(single_row_record)
    predicted_flower_species = FLOWER_SPECIES_NAMES[prediction]

    print(predicted_flower_species[0])

    return '', status.HTTP_200_OK


def _load_model(config):
    """Helper function to hold all info regarding loading in the model"""
    model_objects_folder = config["Model"]["Objects"]["FolderName"]
    pickeled_model_file_name = config["Model"]["Objects"]["ModelFileName"]

    model_location = os.path.join(model_objects_folder, pickeled_model_file_name)

    # Load the model from the file
    return joblib.load(model_location)


def _load_labels(config):
    """Helper function to hold all info regarding loading in the labels"""
    model_objects_folder = config["Model"]["Objects"]["FolderName"]
    target_class_names_file_name = config["Model"]["Objects"][
        "TargetClassLabelNamesFileName"
    ]

    flower_class_names_location = os.path.join(
        model_objects_folder, target_class_names_file_name
    )

    return np.load(flower_class_names_location)


if __name__ == '__main__':

    # this initial process is just brought over from the sample_prediction.py
    with open("./../src/ModelConfig.yaml", "r") as f:
        model_config = yaml.safe_load(f)

    # Load the model from the file based on the config
    MODEL = _load_model(config=model_config)
    app.logger.debug('Model successfully loaded into env')

    # Load in the labels from the file based on the config
    FLOWER_SPECIES_NAMES = _load_labels(config=model_config)
    app.logger.debug('Labels successfully loaded into env')

    app.run()
