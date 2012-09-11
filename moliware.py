# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session
from flaskext.babel import Babel

import os


ACCEPTED_LANGS = ['en', 'es']
DEFAULT_LANG = 'en'


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    if 'lang' in request.args:
        lang = request.args.get('lang')
        if lang in ACCEPTED_LANGS:
            return lang
    return request.accept_languages.best_match(ACCEPTED_LANGS) or DEFAULT_LANG


@app.route('/')
def index(lang=None):
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    debug = 'DEBUG' in os.environ
    app.run(host='0.0.0.0', port=port, debug=debug)