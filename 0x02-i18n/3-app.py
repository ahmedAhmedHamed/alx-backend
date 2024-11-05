#!/usr/bin/env python3
""" initial app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    returns the locale given a request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def hello_world() -> str:
    """ hello_world route """
    return render_template('3-index.html')


if __name__ == '__main__':
    """ launches application """
    app.run()
