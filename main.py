from core.general import *

from lib.init import env

from flask import Flask, render_template
from flask_cors import CORS

from pages.test import app as test

app = Flask(__name__)
CORS(app)
# cors = CORS(app, resources={r"/*": {"origins": "domains"}})

app.register_blueprint(test)

@app.route('/')
def hello():
    return '<h1> ouob </h1><br><b> This is an API site </b>'

if __name__ == '__main__':
    if env('debug'): app.debug = True;
    app.run()
    quit()