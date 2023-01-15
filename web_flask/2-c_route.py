#!/usr/bin/python3

"""
This script starts a Flask Web Application
With two routes
"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ The home page """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """ HBNB Page """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    text = text.replace('_', ' ')

    return 'C {}'.format(escape(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
