# app/__init__.py
from flask import Flask
from flask_googlemaps import GoogleMaps
import config
import os
# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
# app.config.from_object('config')
# app.logger.info(os.getenv("MAP_WIDGETS"))

GoogleMaps(app,key=os.getenv("GOOGLEMAPS_KEY"))

# Load the views
from app import views
from app import tahmo
# from app import services
