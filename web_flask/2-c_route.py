#!/usr/bin/python3
''' python sript that starts a Flask web application '''

from cgitb import text
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    ''' Hello hbnb displayer '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB_display():
    ''' HBNB displayer '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def CisFun(text):
    ''' C displayer '''
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
