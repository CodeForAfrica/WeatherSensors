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
    lasttimeMeasured = sortedTimeSeries[-1]
    lastMeasuredTemp = timeseries["temperature"][sorted(timeseries["temperature"].keys())[-1]]
    lastMeasuredPrecip = timeseries["precipitation"][sorted(timeseries["precipitation"].keys())[-1]]
    lastMeasuredWindSpeed = timeseries["windspeed"][sorted(timeseries["windspeed"].keys())[-1]]
    lastMeasuredWindDirection = timeseries["winddirection"][sorted(timeseries["winddirection"].keys())[-1]]
    lastMeasuredPressure = timeseries["atmosphericpressure"][sorted(timeseries["atmosphericpressure"].keys())[-1]]
    lastMeasuredHumidity = timeseries["relativehumidity"][sorted(timeseries["relativehumidity"].keys())[-1]]
    winddirectionClass = windArrow(lastMeasuredWindDirection)
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
sortedTimeSeries=sortedTimeSeries,
winddirectionClass=winddirectionClass)

@app.route('/stations')
def stations():
    stations = services.get_stations()
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
        style="width:100%; height: 700px",
        markers=marker
    )
    return render_template("stations.html", stationsMap=stationsMap)


@app.route('/station/<station_id>')
def station(station_id):
    station = services.get_station(station_id)
    return render_template("station.html", station=station["station"], timeseries=station["timeseries"])


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
