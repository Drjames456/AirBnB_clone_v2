#!/usr/bin/python3
"A module that start a web flask application"
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Display a greeting message at the root URL.
    Returns 'Hello HBNB!' when the root URL is accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display a simple string at the /hbnb URL.
    Returns 'HBNB'.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by the value of the text variable.
    Underscores in the text variable are replaced with spaces.
    For example, accessing /c/is_fun will display "C is fun".
    """
    text = text.replace('_', ' ')
    return 'C ' + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    If no specific text is provided, 'is cool' is used as the default text.
    Underscores in the text variable are replaced with spaces.
    """
    text = text.replace('_', ' ')
    return 'Python ' + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
