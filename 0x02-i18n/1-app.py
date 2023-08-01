#!/usr/bin/env python3
"""
Basic Flask app with Babel configuration
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Babel configuration
class Config:
    """Config class to set available languages and default locale/timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """Route for the index page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
