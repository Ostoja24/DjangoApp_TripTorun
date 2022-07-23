from django.contrib.gis.db import models

class Trip(models.Model):
    name = models.CharField(max_length=60)
    location = models.PointField()
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=200)