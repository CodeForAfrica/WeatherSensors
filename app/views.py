# views.py

from flask import render_template
from app import app
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import services

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/stations')
def stations():
    stations = services.get_stations()
    markers = []
    for station in stations:
        station["location"]["infobox"] = "<a href=/station/" + station["id"]+">" + station["name"] + "</a>"
        markers.append(station["location"])
    stationsMap = Map(
        identifier="section-map",
        lat=-6.3690,
        lng=38.8888,
        zoom = 7,
        style="width:100%; height: 700px",
        markers=markers
    )
    return render_template("stations.html", stationsMap=stationsMap)

@app.route('/station/<station_id>')
def station(station_id):
    station = services.get_station(station_id)
    return render_template("station.html", station=station["station"], timeseries=station["timeseries"])
