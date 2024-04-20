#!/usr/bin/python3
"Import the Flask class from the flask module"
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
