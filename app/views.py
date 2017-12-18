# views.py

from flask import render_template
from app import app
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import services
import datetime, calendar
import json

@app.route('/')
def index():
    #choosen default station for home, BRT
    station = services.get_station("TA00273")
    timeseries=station['timeseries']
    sortedTimeSeries = sorted(timeseries["temperature"].keys())
    date = datetime.datetime.strptime(sortedTimeSeries[0], '%Y-%m-%dT%H:%M')
    startTime = calendar.timegm(date.utctimetuple()) * 1000
    #startTime = time.mktime(date.utctimetuple())
    #startTime = ((datetime.datetime.strptime(sortedTimeSeries[0], '%Y-%m-%dT%H:%M')).date()).toordinal()
    lasttimeMeasured = sortedTimeSeries[-1]
    lastMeasuredTemp = timeseries["temperature"][lasttimeMeasured]
    lastMeasuredPrecip = timeseries["precipitation"][lasttimeMeasured]
    lastMeasuredWindSpeed = timeseries["windspeed"][lasttimeMeasured]
    lastMeasuredWindDirection = timeseries["winddirection"][lasttimeMeasured]
    lastMeasuredPressure = timeseries["atmosphericpressure"][lasttimeMeasured]
    lastMeasuredHumidity = timeseries["relativehumidity"][lasttimeMeasured]
    print lastMeasuredTemp
    print lastMeasuredWindDirection
    return render_template("index.html",
startTime=startTime,
station=station["station"],
timeseries=timeseries,
lastMeasuredTemp = lastMeasuredTemp,
lastMeasuredPrecip = lastMeasuredPrecip,
lastMeasuredWindSpeed=lastMeasuredWindSpeed,
lastMeasuredWindDirection=lastMeasuredWindDirection,
lastMeasuredPressure=lastMeasuredPressure,
lastMeasuredHumidity=lastMeasuredHumidity,
sortedTimeSeries=sortedTimeSeries)

@app.route('/stations')
def stations():
    stations = services.get_stations()
    markers = []
    for station in stations:
        station["location"]["infobox"] = "<a href=/station/" + station["id"]+">" + station["name"] + "</a>"
        markers.append(station["location"])
    stationsMap = Map(
        identifier="section-map",
        last=-6.3690,
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
