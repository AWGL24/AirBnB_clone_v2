#!/usr/bin/python3
''' Module starts flask service '''

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
