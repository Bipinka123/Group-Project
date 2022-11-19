import json
import requests
import flask
from dotenv import load_dotenv, find_dotenv
import os
import random
from flask_sqlalchemy import SQLAlchemy


load_dotenv(find_dotenv())
app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

@app.route('/login')
def loginPage():
    return flask.render_template('login.html')
