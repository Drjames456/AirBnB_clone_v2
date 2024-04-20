#!/usr/bin/python3
"""
A simple Flask web application to display
basic text messages on different routes.
This module demonstrates basic routing and
documentation standards for Flask applications.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    "Responds to the root URL '/' with a greeting."
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns the string "HBNB" when the '/hbnb' URL is accessed.
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
