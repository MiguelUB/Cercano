"""
This file will run the Flask App
"""
from os import environ

from app import create_app

app = create_app("development")

if __name__ == "__main__":
    app.run(host="0.0.0.0")