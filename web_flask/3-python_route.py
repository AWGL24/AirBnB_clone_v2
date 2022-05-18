#!/usr/bin/python3
''' python sript that starts a Flask web application '''

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    ''' Hello hbnb displayer '''
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB_display():
    ''' HBNB displayer '''
    return "HBNB"


@app.route('/c/<text>')
def CisFun(text):
    ''' C displayer '''
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/(<text>)')
def Pythonis(text='is cool'):
    ''' python displayer '''
    text = text.replace('_', ' ')
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
