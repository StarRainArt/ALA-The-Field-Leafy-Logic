from django.db import models
from datetime import datetime

# Create your models here.

class Device_Data(models.Model):
    serialNumber = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    label = models.CharField(max_length=15)
    lastSeen = models.DateField()
    lastBatteryVoltage = models.IntegerField()

class Soil_Electric_Conductivity_Events(models.Model):
    timeStamp = models.IntegerField(null=True)
    gateWayReceiveTime = models.DateTimeField(default=datetime.now, blank=True)
    device = models.IntegerField()
    value = models.DecimalField(max_digits = 5, decimal_places = 2)

class Soil_Relative_Permittivity_Events(models.Model):
    timeStamp = models.IntegerField()
    gateWayReceiveTime = models.DateTimeField(default=datetime.now, blank=True)
    device = models.IntegerField()
    value = models.DecimalField(max_digits = 5, decimal_places = 2)

class Battery_Voltage_Events(models.Model):
    timeStamp = models.IntegerField()
    gateWayReceiveTime = models.DateTimeField(default=datetime.now, blank=True)
    device = models.IntegerField()
    value = models.DecimalField(max_digits = 5, decimal_places = 2)

class Par_Events(models.Model):
    timeStamp = models.IntegerField()
    gateWayReceiveTime = models.DateTimeField(default=datetime.now, blank=True)
    device = models.IntegerField()
    value = models.DecimalField(max_digits = 5, decimal_places = 2)

class Relative_Humidity_Events(models.Model):
    timeStamp = models.IntegerField()
    gateWayReceiveTime = models.DateTimeField(default=datetime.now, blank=True)
    device = models.IntegerField()
    value = models.DecimalField(max_digits = 5, decimal_places = 2)
