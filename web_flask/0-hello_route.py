#!/usr/bin/python3

"""
This script starts a Flask Web Application
With a single routing
"""


import flask


def create_flask_app():
    """Creates the flask application"""

    app = flask.Flask(__name__)

    @app.route("/", strict_slashes=False)
    def home():
        """ The home page """

        return "Hello HBNB!"

    return app


if __name__ == "__main__":
    create_flask_app().run(host="0.0.0.0", port=5000)
