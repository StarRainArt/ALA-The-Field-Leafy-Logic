from django.contrib import admin
from .models import DeviceData
from .models import DataPoint

# Register your models here.

myModels = [
    DeviceData,
    DataPoint
]

admin.site.register(myModels)