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

def get_locale():
    """Get user's preferred locale if available, otherwise use request header or default"""
    # Check if locale is in URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Check if user is logged in and has a preferred locale
    if g.user and g.user['locale'] and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Use request header to get the best match with supported languages
    header_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # Default to the app's default locale
    return app.config['BABEL_DEFAULT_LOCALE']

@app.before_request
def before_request():
    """Before request function to set user as a global variable"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

@app.route('/')
def index():
    """Route for the index page"""
    return render_template(
        '6-index.html',
        welcome_msg=gettext("You are logged in as %(username)s.") if g.user else gettext("You are not logged in."),
        username=g.user["name"] if g.user else None
    )

if __name__ == "__main__":
    app.run()

