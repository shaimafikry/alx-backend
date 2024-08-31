#!/usr/bin/env python3
""" module of flask"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

# Use Config to set Babel’s default locale ("en") and timezone ("UTC").
class Config:
    """CONFIG CLASS """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# to add config from an object
app.config.from_object(Config)
babel = Babel(app)

@app.route('/')
def home():
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
