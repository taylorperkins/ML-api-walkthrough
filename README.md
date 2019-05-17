## Flask implementation for predictive endpoints

Given a model, can you deploy it?
Ok, that's a lot of steps..
Let's start small by adding an api around a  simple model.

The api I will be using is [Flask-API](https://www.flaskapi.org/) since there is no supporting a frontend.
While not as fast as some, or as robust as others, it's familiarity and simplicity make me feel most comfortable. 

## Setup
Have the following installed:
* python3.7
* pipenv

To get started with your environment, run: 
```
pipenv install --dev
```

This should install everything listed from within the [Pipfile](./Pipfile) provided.

Since this is a flask app, there are a couple things you will need to run it locally.
I have set up the entire app within [api.py](src/api.py) for simplicity for now.

From your CLI interface, run:
```
(ML-api-walkthrough) >> cd src
(ML-api-walkthrough) >> gunicorn --bind 0.0.0.0:8000 wsgi
```

To test the endpoints listed in [pass_my_requests.py](./src/pass_my_requests.py), run the following in the src directory:
```
(ML-api-walkthrough) >> python test_requests.py
```


## Running Tests (MVP)
We are using [locustio])(https://locust.io/) to run simulated tests against the endpoints provided.
With your application up and running from above..
Here is how you can get started testing out those endpoints:
```
(ML-api-walkthrough) >> locust --host=http://0.0.0.0:8000 -f ./src/tests/locustfile.py
```

This should allow you then visit [this page](http://127.0.0.1:8089/) to input a number of users, and a hatch rate for the simulations.
Once you click "Start Swarming", you will be brought to a new page that shows you some stats around the simulations such as number of requests, number of fails, avg min and max times.


