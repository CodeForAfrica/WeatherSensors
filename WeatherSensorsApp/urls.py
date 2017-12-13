from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^station/$', views.station, name='station'),
    url(r'^station/(?P<station_id>.*[0-9]{5})/$', views.detail, name='detail'),
    url(r'^station/(?P<station_id>.*[0-9]{5})/hourly/$', views.timeseries, name='timeseries')
]
