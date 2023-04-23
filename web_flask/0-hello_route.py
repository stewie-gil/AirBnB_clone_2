#!/usr/bin/python3
""" This a flask script for the hbnb app. """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Flask app Displays 'Hello HBNB!'.
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
