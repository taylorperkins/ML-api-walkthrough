"""
This is a list of dictionaries, each of which contains a sample request and expected response your API should return.
It's up to you whether your programmatically POST the requests to your API endpoint, or provide us with sample curl commands.
"""
request_and_responses = [
    {
        "Request": {
            "FlowerID": 1,
            "SepalLength": 4.9,
            "SepalWidth": 2.5,
            "PetalLength": 4.5,
            "PetalWidth": 1.7
        },
        "ExpectedResponse": {"FlowerID": 1, "Species:": "versicolor"},
    },
    {
        "Request": {
            "FlowerID": 2,
            "SepalLength": 4.9,
            "SepalWidth": 4,
            "PetalLength": 4.5,
            "PetalWidth": 4
        },
        "ExpectedResponse": {"FlowerID": 2, "Species:": "virginica"},
    },
    {
        "Request": {
            "FlowerID": 3,
            "SepalLength": 1.0,
            "SepalWidth": 1.6,
            "PetalLength": 1.1,
            "PetalWidth": 1.5
        },
        "ExpectedResponse": {"FlowerID": 3, "Species:": "setosa"},
    },
]
