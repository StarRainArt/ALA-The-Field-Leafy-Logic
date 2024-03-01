from django.db import models
from datetime import datetime

# Create your models here.

class DeviceData(models.Model):
    device_id = models.IntegerField()
    serialNumber = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    last_seen = models.IntegerField()
    last_battery_voltage = models.FloatField()
    human_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "devicedata"

class DataPoint(models.Model):
    timeStamp = models.IntegerField()
    gate_way_receive_time = models.DateTimeField() #default=datetime.now, blank=True
    device = models.IntegerField()
    value = models.DecimalField(max_digits = 15, decimal_places = 2)
    human_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "datapoint"
