from flask import Flask

app = Flask(__name__)
app.config.from_object('config') # tell Flask to read the config file and use it

from app import views
