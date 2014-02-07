from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') # tell Flask to read the config file and use it
db = SQLAlchemy(app) # initialize database

from app import views, models

