# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flaskext.babel import Babel

import os


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(['es', 'en']) or 'en'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)