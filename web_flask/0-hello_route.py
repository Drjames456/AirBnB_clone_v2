#!/usr/bin/python3
"""
A simple Flask web application to display basic text messages on different routes.
The application defines two routes:
- The root ('/') which returns "Hello HBNB!"
- '/hbnb' which returns "HBNB"
This module demonstrates basic routing and documentation standards for Flask applications.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Responds to the root URL '/' with a greeting.
    This function returns a simple string "Hello HBNB!" when the root URL is accessed.
    It demonstrates how to handle root-level HTTP GET requests in a Flask application.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Responds to the URL '/hbnb' with a specific text.
    This function returns the string "HBNB" when the '/hbnb' URL is accessed.
    It demonstrates the use of non-root level routes in a Flask application.
    """
    return "HBNB"

if __name__ == '__main__':
    """
    Executes the Flask application only if the script is run directly.
    This block sets the Flask application to run on all network interfaces of the host
    and listens on port 5000.
    """
    app.run(host='0.0.0.0', port=5000)

