# app/__init__.py
from flask import Flask
from flask_googlemaps import GoogleMaps

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')

GoogleMaps(app)

# Load the views
from app import views
from app import services
