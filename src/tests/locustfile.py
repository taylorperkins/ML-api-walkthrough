from locust import HttpLocust, TaskSet, task


class AllEndpoints(TaskSet):

    def on_start(self):
        # probably dont need anything here.
        pass

    def on_stop(self):
        # probably dont need anything here.
        pass

    @task(1)
    def health(self):
        """Making sure that the health endpoint is up and running"""
        self.client.get("/health")

    @task(3)
    def predict(self):
        # grabbed one from the example for now.
        self.client.post("/predict", {
            "FlowerID": 2,
            "SepalLength": 4.9,
            "SepalWidth": 4,
            "PetalLength": 4.5,
            "PetalWidth": 4
        })


class ModelAPI(HttpLocust):
    task_set = AllEndpoints

    # should play with these
    min_wait = 5000
    max_wait = 9000
