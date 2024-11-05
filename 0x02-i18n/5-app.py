#!/usr/bin/env python3
""" initial app """
import flask
from flask import Flask, render_template, request
from flask_babel import Babel


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


def get_user():
    """ returns a user dictionary or None
     if the ID cannot be found or if login_as was not passed. """
    login_as = request.args.get('login_as')
    if login_as is None:
        return None
    global users
    return users.get(int(login_as))


@app.before_request
def before_request():
    """ happens before request """
    flask.g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    returns the locale given a request
    """
    locale = request.args.get('locale')
    if locale:
        for lang in app.config['LANGUAGES']:
            if lang == locale:
                return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """ hello_world route """
    user = flask.g.user
    if user is not None:
        user = user["name"]
    return render_template('5-index.html', user=user)


if __name__ == '__main__':
    """ launches application """
    app.run()
