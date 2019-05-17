"""Entry point for gunicorn"""
from api import api as application


if __name__ == "__main__":
    application.run()
