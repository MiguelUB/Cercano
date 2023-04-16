from os import environ

import psycopg2
from flask import Flask

from config.cofig import app_config
from config.db import db


def create_app(config_name):
    """
    Construct the core app object.

    :param config_name: The type of configuration we will use
    (development, preproduction, production)
    :return: The Flask Aplication
    """
    app = Flask(__name__, instance_relative_config=True)

    # Application Configuration
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    #login_manager.init_app(app)
    app.secret_key = environ["APP_SECRET_KEY"]


    with app.app_context():

        return app