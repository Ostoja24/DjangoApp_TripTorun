from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Trip

# @admin.register(Trip)
# class TripAdministrator(LeafletGeoAdmin):
#     list_display = ('name', 'location')
admin.site.register(Trip, LeafletGeoAdmin)
# Register your models here.
