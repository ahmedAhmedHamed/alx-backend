#!/usr/bin/env python3
""" initial app """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route("/")
def hello_world() -> str:
    """ hello_world route """
    return render_template('1-index.html')


if __name__ == '__main__':
    """ launches application """
    app.run()
