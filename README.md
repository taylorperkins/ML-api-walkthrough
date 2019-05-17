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
pipenv install
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