define USAGE
Simple api to support predicing against an iris classification model.

Commands:
	init				Install py dependencies with pipenv
	serve 				Run the api locally using gunicorn
	build				Build and run a docker image for this application
	locust-test			Run locust tests for the api
	pass-my-requests	Serves up the api, then runs the test script for sample predictions
endef

export USAGE
help:
	@echo "$$USAGE"

init:
	pip3 install pipenv
	pipenv install --dev --skip-lock
	pipenv shell

serve:
	gunicorn -b 0.0.0.0:8000 --chdir src api

build:
	docker build --tag flask_gunicorn_app .
	docker run --detach -p 8000:80 flask_gunicorn_app
	@echo "Docker image up in the clouds.."
	@echo "Api available for use! Try going http://0.0.0.0:8000/health"

locust-test:
	@echo "Hey.. You should go here: http://127.0.0.1:8089/"
	@locust --host=http://0.0.0.0:8000 -f src/tests/locustfile.py

pass-my-requests:
	python src/test_requests.py
