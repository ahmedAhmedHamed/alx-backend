#!/usr/bin/env python3
""" initial app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    """ hello_world route """
    return render_template('0-index.html')


if __name__ == '__main__':
    """ launches application """
    app.run()
