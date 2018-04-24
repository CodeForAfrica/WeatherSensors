# views.py

from flask import render_template
from app import app
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from services import tahmo
import datetime, calendar
import json
import logging
import os

@app.route('/')
def index():
    #choosen default station for home, BRT
    stations = tahmo.get_stations()
    station = tahmo.get_station(os.getenv("DEFAULT_STATION"))
    if bool(station['timeseries']):
        timeseries=station['timeseries']
        sortedTimeSeries = sorted(timeseries["temperature"].keys())
        date = datetime.datetime.strptime(sortedTimeSeries[0], '%Y-%m-%dT%H:%M')
        startTime = calendar.timegm(date.utctimetuple()) * 1000
        lasttimeMeasured = sortedTimeSeries[-1]
        if "temperature" in timeseries:
            lastMeasuredTemp = timeseries["temperature"][sorted(timeseries["temperature"].keys())[-1]]
        else:
            lastMeasuredTemp = "No record"
        if "precipitation" in timeseries:
            lastMeasuredPrecip = timeseries["precipitation"][sorted(timeseries["precipitation"].keys())[-1]]
        else:
            lastMeasuredPrecip = "No record"
        if "windspeed" in timeseries:
            lastMeasuredWindSpeed = timeseries["windspeed"][sorted(timeseries["windspeed"].keys())[-1]]
        else:
            lastMeasuredWindSpeed = "No record"
        if "winddirection" in timeseries:
            lastMeasuredWindDirection = timeseries["winddirection"][sorted(timeseries["winddirection"].keys())[-1]]
        else:
            lastMeasuredWindDirection = "No record"
        if "atmosphericpressure" in timeseries:
            lastMeasuredPressure = timeseries["atmosphericpressure"][sorted(timeseries["atmosphericpressure"].keys())[-1]]
        else:
            lastMeasuredPressure = "No record"
        if "relativehumidity" in timeseries:
            lastMeasuredHumidity = timeseries["relativehumidity"][sorted(timeseries["relativehumidity"].keys())[-1]]
        else:
            lastMeasuredHumidity = "No record"
        winddirectionClass = windArrow(lastMeasuredWindDirection)
        return render_template("index.html",
    startTime=startTime,
    stations=stations,
    station=station["station"],
    timeseries=timeseries,
    lastMeasuredTemp = lastMeasuredTemp,
    lastMeasuredPrecip = lastMeasuredPrecip,
    lastMeasuredWindSpeed=lastMeasuredWindSpeed,
    lastMeasuredWindDirection=lastMeasuredWindDirection,
    lastMeasuredPressure=lastMeasuredPressure,
    lastMeasuredHumidity=lastMeasuredHumidity,
    sortedTimeSeries=sortedTimeSeries,
    winddirectionClass=winddirectionClass)
    else:
        station = station['station']
        message = "Station " + station["name"] + " has no recorded timeseries"
        return render_template('404.html', message=message, stations=stations), 404
@app.route('/station')
def stations():
    stations = tahmo.get_stations()
    marker = []
    for station in stations:
        station["location"]["infobox"] = "<a href=/station/" + station["id"]+">" + station["name"] + "</a>"
        marker.append(station["location"])
    print marker
    stationsMap = Map(
        identifier="section-map",
        lat=-6.3690,
        lng=38.8888,
        zoom = 7,
        style="width:100%; height: 500px",
        markers=marker
    )
    return render_template("stations.html", stations=stations,stationsMap=stationsMap)


@app.route('/station/<station_id>')
def station(station_id):
    stations = tahmo.get_stations()
    station = tahmo.get_station(station_id)
    if bool(station['timeseries']):
        timeseries=station['timeseries']
        sortedTimeSeries = sorted(timeseries["temperature"].keys())
        date = datetime.datetime.strptime(sortedTimeSeries[0], '%Y-%m-%dT%H:%M')
        startTime = calendar.timegm(date.utctimetuple()) * 1000
        lasttimeMeasured = sortedTimeSeries[-1]
        if "temperature" in timeseries:
            lastMeasuredTemp = timeseries["temperature"][sorted(timeseries["temperature"].keys())[-1]]
        else:
            lastMeasuredTemp = "No record"
        if "precipitation" in timeseries:
            lastMeasuredPrecip = timeseries["precipitation"][sorted(timeseries["precipitation"].keys())[-1]]
        else:
            lastMeasuredPrecip = "No record"
        if "windspeed" in timeseries:
            lastMeasuredWindSpeed = timeseries["windspeed"][sorted(timeseries["windspeed"].keys())[-1]]
        else:
            lastMeasuredWindSpeed = "No record"
        if "winddirection" in timeseries:
            lastMeasuredWindDirection = timeseries["winddirection"][sorted(timeseries["winddirection"].keys())[-1]]
        else:
            lastMeasuredWindDirection = "No record"
        if "atmosphericpressure" in timeseries:
            lastMeasuredPressure = timeseries["atmosphericpressure"][sorted(timeseries["atmosphericpressure"].keys())[-1]]
        else:
            lastMeasuredPressure = "No record"
        if "relativehumidity" in timeseries:
            lastMeasuredHumidity = timeseries["relativehumidity"][sorted(timeseries["relativehumidity"].keys())[-1]]
        else:
            lastMeasuredHumidity = "No record"
        winddirectionClass = windArrow(lastMeasuredWindDirection)
        return render_template("station.html",
    startTime=startTime,
    stations=stations,
    station=station["station"],
    timeseries=timeseries,
    lastMeasuredTemp = lastMeasuredTemp,
    lastMeasuredPrecip = lastMeasuredPrecip,
    lastMeasuredWindSpeed=lastMeasuredWindSpeed,
    lastMeasuredWindDirection=lastMeasuredWindDirection,
    lastMeasuredPressure=lastMeasuredPressure,
    lastMeasuredHumidity=lastMeasuredHumidity,
    sortedTimeSeries=sortedTimeSeries,
    winddirectionClass=winddirectionClass)
    else:
        station = station['station']
        message = "Station " + station["name"] + " has no recorded timeseries"
        return render_template('404.html', message=message, stations=stations), 404

@app.errorhandler(404)
def page_not_found(e):
    stations = tahmo.get_stations()
    message = "Page not found"
    return render_template('404.html', message=message, stations=stations), 404

@app.errorhandler(403)
def page_not_found(e):
    stations = tahmo.get_stations()
    message = "Page is forbidden"
    return render_template('404.html', message=message, stations=stations), 403

@app.errorhandler(410)
def page_not_found(e):
    stations = tahmo.get_stations()
    message = "Page is gone"
    return render_template('404.html', message=message, stations=stations), 410

@app.errorhandler(500)
def page_not_found(e):
    stations = tahmo.get_stations()
    message = "Internal Error"
    return render_template('404.html', message=message, stations=stations), 500

@app.errorhandler(501)
def page_not_found(e):
    stations = tahmo.get_stations()
    message = "Internal Error"
    return render_template('404.html', message=message, stations=stations), 501

def windArrow(winddirection):
    if winddirection >= 12 and winddirection < 33.5:
        return "nne"
    elif winddirection >= 33.5 and winddirection < 56:
        return "ne"
    elif winddirection >= 56 and winddirection < 78.5:
        return "ene"
    elif winddirection >= 78.5 and winddirection < 81:
        return "e"
    elif winddirection >= 81 and winddirection < 123.5:
        return "ese"
    elif winddirection >= 123.5 and winddirection < 146:
        return "se"
    elif winddirection >= 146 and winddirection < 168.5:
        return "sse"
    elif winddirection >= 168.5 and winddirection < 191:
        return "s"
    elif winddirection >= 191 and winddirection < 113.5:
        return "ssw"
    elif winddirection >= 113.5 and winddirection < 236:
        return "sw"
    elif winddirection >= 236 and winddirection < 258.5:
        return "wsw"
    elif winddirection >= 258.5 and winddirection < 281:
        return "w"
    elif winddirection >= 281 and winddirection < 303.5:
        return "wnw"
    elif winddirection >= 303.5 and winddirection < 326:
        return "nw"
    elif winddirection >= 326 and winddirection < 348.5:
        return "nnw"
    else:
        return ""
