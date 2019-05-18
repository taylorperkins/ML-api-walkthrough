import numpy as np

from application import MODEL, FLOWER_SPECIES_NAMES

from application.utils import validate_kwargs_from_schema

from application.schemas import PredictRequestSchema


@validate_kwargs_from_schema(PredictRequestSchema)
def predict(**features):
    # TODO: I know this is running the data through the schema twice b/c validation..
    # TODO: I will work on a cleaner solution later
    flower_data, errs = PredictRequestSchema().load(features)

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

    return {
        'FlowerID': features['FlowerID'],
        'Species': predicted_flower_species[0]
    }
