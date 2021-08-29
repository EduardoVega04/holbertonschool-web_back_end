#!/usr/bin/env python3

"""Route module for the API 	"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """ return index"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
