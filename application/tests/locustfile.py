from random import randint, uniform, choice

from locust import HttpLocust, TaskSet, task


class AllEndpoints(TaskSet):

    def on_start(self):
        # health check at start
        self.client.get("/health")

    def on_stop(self):
        # probably dont need anything here.
        pass

    @task(3)
    def test_predict__success(self):
        # grabbed one from the example for now.
        self.client.post("/predict", {
            "FlowerID": 2,
            "SepalLength": uniform(1.0, 5.0),
            "SepalWidth": uniform(1.0, 5.0),
            "PetalLength": uniform(1.0, 5.0),
            "PetalWidth": uniform(1.0, 5.0)
        })

    @task(3)
    def test_predict__invalid_predict_body_missing_features_raises_400(self):
        """Right now, all of the fields are required.
        If the client sends in a body without one of the fields (or without many),
        we want to assert that the response status code is a 404

        """
        available_fields = [
            "SepalLength",
            "SepalWidth",
            "PetalLength",
            "PetalWidth"]

        data = dict(flower_id=randint(1, 200))

        # pick random fields from the list to build out dynamic request bodies
        for i in range(randint(1, len(available_fields))):
            key = choice(available_fields)
            _ = available_fields.pop(available_fields.index(key))

            data.update({key: uniform(1.0, 5.0)})

        with self.client.post("/predict", data, catch_response=True) as response:
            if response.status_code == 400:
                response.success()

    @task(3)
    def test_predict__invalid_predict_body_missing_flower_id_raises_400(self):
        """Making sure that we return 400 when no flowerid is in the
        request body
        """

        available_fields = [
            "SepalLength",
            "SepalWidth",
            "PetalLength",
            "PetalWidth"]

        data = {key: uniform(1.0, 5.0) for key in available_fields}

        with self.client.post("/predict", data, catch_response=True) as response:
            if response.status_code == 400:
                response.success()

    @task(3)
    def test_predict__invalid_feature_data_values_raises_400(self):
        """We are using marshmallow schema to validate the incoming request.
        It should fail when we get inappropriate values as input.
        """

        available_fields = [
            "SepalLength",
            "SepalWidth",
            "PetalLength",
            "PetalWidth"]

        data = {key: uniform(1.0, 5.0) for key in available_fields}

        # TODO: maybe also add a threshold?? negative values are inappropriate,
        # TODO: as well as values above a certain amount.
        invalid_fields = [None, 'cat', 'dog', True, False, [1.5, 2.6], {'key': 'value'}]

        data[choice(available_fields)] = choice(invalid_fields)

        with self.client.post("/predict", data, catch_response=True) as response:
            if response.status_code == 400:
                response.success()


class ModelAPI(HttpLocust):
    task_set = AllEndpoints

    # should play with these
    min_wait = 5000
    max_wait = 9000
