#!/usr/bin/python3
"""Initial flask app"""
from flask import flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Renders return content in the home route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
