#!/usr/bin/python3

"""
This script starts a Flask Web Application
"""


import flask


app = flask.Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ The home page """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """Route to hbnb page"""

    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
