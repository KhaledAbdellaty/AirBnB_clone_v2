#!/usr/bin/python3
"""A Flask web application.

runs on host=0.0.0.0, port=5000"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """The initial route that displays, 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbhb_route():
    """The '/hbnb route that displays, 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """The '/c/' route that take variable and display it"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is_cool'):
    """The '/python/' route have default value and accepts variable"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """It's accept only int variable, it's called variable rule"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_number_templete(n):
    """Render template and pass dynamic data using Jinja2"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_number_od_or_even(n):
    """Render template and pass dynamic data using Jinja2"""
    if (n % 2) == 0:
        x = 'even'
    else:
        x = 'odd'
    return render_template("6-number_odd_or_even.html", n=n, x=x)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
