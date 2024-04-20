#!/usr/bin/python3
"A module that a script that starts a Flask web application"
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Route for the root or home page. Returns a greeting. """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Route for '/hbnb'. Returns a short string. """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C ' followed by the value of the text variable.
    Underscores in the text variable are replaced with spaces.
    Example: accessing /c/is_fun will display "C is fun".
    """
    # Replace underscores with spaces in the text variable
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
