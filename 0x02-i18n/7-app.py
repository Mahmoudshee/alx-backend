#!/usr/bin/env python3
"""
Flask app with Babel configuration, locale selection, time zone selection, and parametrized templates
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)

# Babel configuration
class Config:
    """Config class to set available languages, default locale, and default timezone"""
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
    # ... (same as in Task 6)

def get_timezone():
    """Get user's preferred time zone if available, otherwise use user settings or default to UTC"""
    # Check if timezone is in URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate the timezone
            import pytz
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check if user is logged in and has a preferred timezone
    if g.user and g.user['timezone']:
        try:
            # Validate the timezone
            import pytz
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to the app's default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']

@app.before_request
def before_request():
    """Before request function to set user as a global variable"""
    # ... (same as in Task 6)

@app.route('/')
def index():
    """Route for the index page"""
    # ... (same as in Task 6)

if __name__ == "__main__":
    app.run()

