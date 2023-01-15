#!/usr/bin/python3

"""
This script starts a Flask Web Application
With two routes
"""


from flask import Flask
from flask import render_template
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
    """ C is fun page """

    text = text.replace('_', ' ')

    return 'C {}'.format(escape(text))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """Python is cool Page"""

    text = text.replace('_', ' ')

    return "Python {}".format(escape(text))


@app.route("/number/<int:n>")
def is_a_number(n):
    """Is it a number page? """

    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Number Template """

    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """ Number Odd or Even page """

    if (n % 2 == 0):
        text = "even"
    else:
        text = "odd"

    return render_template('6-number_odd_or_even.html', n=n, type=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
