from django.shortcuts import render
from django.http import HttpResponse
import services
import json

# Create your views here.
def index(request):
    return HttpResponse("Hi, you're looking at weather sensor data.")

def station(request):
    stations = services.get_stations()
    return HttpResponse("Hi, you're looking at station list." + json.dumps(stations))

def detail(request, station_id):
    station = services.get_station(station_id)
    return HttpResponse("Hi, you're looking at station list." + json.dumps(station))

def timeseries(request, station_id):
    startDate = request.GET.get('startDate', '')
    endDate = request.GET.get('endDate', '')
    timeseries = services.get_timeseries(station_id, startDate, endDate)
    return HttpResponse("Hi, you're looking at station list." + json.dumps(timeseries))
