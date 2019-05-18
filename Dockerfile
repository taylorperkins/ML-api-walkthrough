# start here
FROM python:3.7

# go ahead and keep the original structure for now
# not super pumped about sticking the model in there..
# but it's small enough
ADD application /app

WORKDIR /app

# skip pipenv since it's just in a container
RUN pip install -e .

WORKDIR /app

EXPOSE 80

# run the app
CMD ["gunicorn", "-b", "0.0.0.0:80", "application:api"]
