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

All commands you could need to get around this application are short-handed for you through [this Makefile](./Makefile).
I will list out the different commands here if you want to take advantage of them.. 
Otherwise, I will link the commands to the more expressive version.

### Application Commands:
* [**_make init_**](#getting-started)
    * Creates a brand new pipenv for ya via `pip3`
    * Installs everything from scratch
    * Activates the environment
    
* [**_make serve_**](#serving-the-app)
    * Runs the api via gunicorn
    
* [**_make build_**](#running-in-docker)
    * Builds a docker image for the api
    * Runs the app behind the scenes
    
* [**_make locust-test_**](#running-tests)
    * Spins up the locust tests for the api
   
* [**_make pass-my-requests_**](#example-requests)
    * *Pre-req*: please have the api running locally first via a separate command, otherwise you will get some undesirable messages.
    * Runs a python script that pings the `/predict` endpoint with a set of pre-determined values.
    It will yell at ya if something is wrong, otherwise it will "Success" at ya if something is right.
    

## Getting started!
To get started with your environment, run: 
```bash
pipenv install --dev --skip-lock -e application/
pipenv shell
```

This should install everything listed from within the [setup.py](./application/setup.py) that is being used 
within the application.

Since this is a flask app, there are a couple things you will need to run it locally.
I have set up the entire app within [api.py](src/api.py) for simplicity for now.

## Serving the app

From your CLI interface, run:
```bash
gunicorn -b 0.0.0.0:8000 --chdir application application:api
```

## Example requests
To test the endpoints listed in [pass_my_requests.py](./src/pass_my_requests.py), run the following in the src directory:
```bash
python application/tests/test_requests.py
```


## Running Tests
We are using [locustio])(https://locust.io/) to run simulated tests against the endpoints provided.
With your application up and running from above..
Here is how you can get started testing out those endpoints:
```bash
locust --host=http://0.0.0.0:8000 -f application/tests/locustfile.py
```

This should allow you then visit [this page](http://127.0.0.1:8089/) to input a number of users, and a hatch rate for the simulations.
Once you click "Start Swarming", you will be brought to a new page that shows you some stats around the simulations such as number of requests, number of fails, avg min and max times.

## Running in docker!
_Pre-req_: Make sure you are in the root folder for this project

Also included in this application is a Dockerfile to allow you to build an image and serve it up for further use.
This image is using everything that has already been used up to this point. 
Some commands to get you started with the docker image:
```bash
docker build --tag flask_gunicorn_app .
docker run --detach -p 80:8000 flask_gunicorn_app
```

Once everything clears up in your terminal, you should then be able to access the api again. 
Try running this bad boi.
```bash
curl -X GET "http://0.0.0.0:8000/health"
```
