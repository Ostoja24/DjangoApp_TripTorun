from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from js2py import translate_file

from .models import Trip
from django.shortcuts import render
import js2py
from django.contrib.gis.geos import Point
from django.views.generic import TemplateView
from django.shortcuts import render
import geocoder
# Create your views here.
gps = geocoder.ip('me')
string_gps = gps.latlng

longitude = string_gps[1]
latitude = string_gps[0]

user_gps = Point(longitude, latitude, srid=4326)
def home(request):
    return render(request,'trips/index.html')

