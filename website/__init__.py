from flask import Flask
from os import path, environ
from secrets import token_hex

def create_app():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = get_secret_key("SECRET_KEY.txt")

    from .views import blueprint
    app.register_blueprint(blueprint, url_prefix="/")

    return app

def get_secret_key(filename):

    if "SECRET_KEY" in environ:
        return environ["SECRET_KEY"]

    if path.exists(filename):
        with open(filename, "r") as file:
            return file.read()

    key = token_hex(32)  # Generates a 64-character hex string
    with open(filename, "w") as file:
        file.write(key)
    return key
