#!/usr/bin/env python3
"""
Flask app with Babel configuration, locale selection, and parametrized templates
"""

from flask import Flask, render_template, request, g
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

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """Retrieve user from the user table based on user_id"""
    return users.get(user_id)

@app.before_request
def before_request():
    """Before request function to set user as a global variable"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

@app.route('/')
def index():
    """Route for the index page"""
    return render_template(
        '5-index.html',
        welcome_msg=gettext("You are logged in as %(username)s.") if g.user else gettext("You are not logged in."),
        username=g.user["name"] if g.user else None
    )

if __name__ == "__main__":
    app.run()

