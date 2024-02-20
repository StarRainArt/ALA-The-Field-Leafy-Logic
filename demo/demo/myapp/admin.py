from django.contrib import admin

from .models import Device_Data
from .models import Soil_Electric_Conductivity_Events
from .models import Soil_Relative_Permittivity_Events
from .models import Battery_Voltage_Events
from .models import Par_Events
from .models import Relative_Humidity_Events
from .models import soil_temperature_events

# Register your models here.

myModels = [
    Device_Data,
    Soil_Electric_Conductivity_Events,
    Soil_Relative_Permittivity_Events,
    Battery_Voltage_Events,
    Par_Events,
    Relative_Humidity_Events,
    soil_temperature_events
]

admin.site.register(myModels)
