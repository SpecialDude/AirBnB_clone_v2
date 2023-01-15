#!/usr/bin/python3

"""
This script starts a Flask Web Application
With two routes
"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ The home page """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """ HBNB Page """

    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
