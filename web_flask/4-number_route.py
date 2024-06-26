#!/usr/bin/python3
"A module that starts a Flask web application"
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Returns a greeting message at the root URL. """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns the string 'HBNB' at the '/hbnb' URL. """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns 'C' followed by the value of the text variable,
    with underscores replaced by spaces.
    Example: Accessing /c/hello_world displays "C hello world".
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Returns 'Python' followed by the value of
    the text variable or the default value 'is cool'.
    Underscores in the text are replaced with spaces.
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays the message 'n is a number' only if n is an integer.
    Example: Accessing /number/42 displays "42 is a number".
    """
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
