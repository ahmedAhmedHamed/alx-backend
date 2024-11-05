#!/usr/bin/env python3
""" initial app """
from datetime import datetime
from typing import Union, Dict

import flask
from flask import Flask, render_template, request
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


def is_valid_timezone(tz):
    """ checks if tz is a valid timezone """
    try:
        pytz.timezone(tz)
        return True
    except UnknownTimeZoneError:
        return False


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as) -> Union[Dict[str, Union[str, None]], None]:
    """ returns a user dictionary or None
     if the ID cannot be found or if login_as was not passed. """
    if login_as is None:
        return None
    return users.get(int(login_as))


@babel.localeselector
def get_locale() -> str:
    """
    returns the locale given a request
    """
    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale:
        for lang in app.config['LANGUAGES']:
            if lang == locale:
                return lang
    # Locale from user settings
    if flask.g.user:
        locale = flask.g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    returns the tz given a request
    """
    # tz from URL parameters
    tz = request.args.get('locale')
    if tz and is_valid_timezone(tz):
        return tz
    # tz from user settings
    if flask.g.user:
        tz = flask.g.user.get('timezone')
        if tz and is_valid_timezone(tz):
            return tz
    return "UTC"


@app.before_request
def before_request():
    """ happens before request """
    flask.g.user = get_user(request.args.get('login_as'))
    flask.g.current_time = datetime.now(pytz.timezone(get_timezone()))


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """ hello_world route """
    return render_template('index.html')


if __name__ == '__main__':
    """ launches application """
    app.run()
