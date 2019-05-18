# start here
FROM python:3.7

# go ahead and keep the original structure for now
# not super pumped about sticking the model in there..
# but it's small enough
ADD ./src /app/src
ADD ./model_objects /app/model_objects

# Pipfile and lock
ADD Pipfile* /app/

WORKDIR /app

# trying to keep it same as whats going on on my machine.
RUN pip install pipenv
RUN pipenv install --system --deploy

WORKDIR /app/src

EXPOSE 80

# run the app
CMD ["gunicorn", "-b", "0.0.0.0:80", "api"]
