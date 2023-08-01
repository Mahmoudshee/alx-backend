#!/usr/bin/env python3
"""
Flask app with Babel configuration, locale selection, time zone selection, and parametrized templates
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz
from datetime import datetime

app = Flask(__name__)

# Babel configuration
# ... (same as in Task 7)

# Mock user table
# ... (same as in Task 7)

# Functions to get user and infer time zone
# ... (same as in Task 7)

@app.route('/')
def index():
    """Route for the index page"""
    user = g.user
    current_time = None
    if user and user.get('timezone'):
        try:
            # Get the user's preferred time zone
            user_timezone = pytz.timezone(user['timezone'])
            # Get the current time in the user's time zone
            current_time = datetime.now(user_timezone).strftime("%b %d, %Y, %I:%M:%S %p")
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.locale == 'fr':
        welcome_msg = gettext("Nous sommes le %(current_time)s.")
    else:
        welcome_msg = gettext("The current time is %(current_time)s.")

    return render_template('7-index.html', welcome_msg=welcome_msg % {'current_time': current_time})

if __name__ == "__main__":
    app.run()

