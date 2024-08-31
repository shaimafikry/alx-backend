#!/usr/bin/env python3
from flask import Flask, request, render_template
from flask_babel import Babel, _

# Define the configuration class
class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Initialize Flask app
app = Flask(__name__)

# Apply the configuration to the app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

# Define locale selector to choose the language based on request
@babel.localeselector
def get_locale():
    # Check URL parameters first
    lang = request.args.get('lang')
    if lang in app.config['LANGUAGES']:
        return lang
    
    # If no URL parameter, use the best match from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
