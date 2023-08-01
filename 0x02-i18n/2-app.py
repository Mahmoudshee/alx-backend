#!/usr/bin/env python3
"""
Flask app with Babel configuration and locale selection
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)

# Babel configuration
class Config:
    """Config class to set available languages and default locale/timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for the supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route for the index page"""
    return render_template('2-index.html', welcome_msg=gettext("Welcome to Holberton"))


if __name__ == "__main__":
    app.run()
