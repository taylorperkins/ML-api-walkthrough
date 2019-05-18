from sklearn.externals import joblib
import numpy as np
import os
import yaml


with open("ModelConfig.yaml", "r") as f:
    config = yaml.safe_load(f)


model_objects_folder = config["Model"]["Objects"]["FolderName"]
pickeled_model_file_name = config["Model"]["Objects"]["ModelFileName"]
target_class_names_file_name = config["Model"]["Objects"][
    "TargetClassLabelNamesFileName"
]


model_location = os.path.join(model_objects_folder, pickeled_model_file_name)

flower_class_names_location = os.path.join(
    model_objects_folder, target_class_names_file_name
)


# Load the model from the file
knn_from_joblib = joblib.load(model_location)


sepal_length = 1.0
sepal_width = 1.6
petal_length = 1.1
petal_width = 1.5
petal_width_cubed = np.power(petal_width, 3)

single_row_record = np.array(
    [sepal_length, sepal_width, petal_length, petal_width, petal_width_cubed]
).reshape(1, -1)

prediction = knn_from_joblib.predict(single_row_record)


flower_species_names = np.load(flower_class_names_location)

predicted_flower_species = flower_species_names[prediction]
print(predicted_flower_species)
print("Success running sample predictions!")
