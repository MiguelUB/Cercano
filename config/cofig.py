"""
File configuration that sets different variables to the Flask App configuration
"""
import os
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
cercano_path = path.join(basedir, "..")
load_dotenv(path.join(cercano_path, ".env"))


class Config(object):
    """Set Flask configuration from environment variables."""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{pw}@{url}/{db}".format(
        user=environ["POSTGRES_USER"],
        pw=environ["POSTGRES_PWD"],
        url=environ["POSTGRES_URL"],
        db=environ["POSTGRES_DB"],
    )



class DevelopmentConfig(Config):
    """Set variables to Flask configuration for Development"""

    DEBUG = True


class ProductionConfig(Config):
    """Set variables to Flask configuration for Production"""

    DEBUG = False


class PreProductionConfig(Config):
    """Set variables to Flask configuration for Pre-Production"""

    DEBUG = False


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "preproduction": PreProductionConfig,
}
