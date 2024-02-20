import requests
import time
from django.utils import timezone

from .models import Device_Data
from .models import Soil_Electric_Conductivity_Events
from .models import Soil_Relative_Permittivity_Events
from .models import Battery_Voltage_Events
from .models import Par_Events
from .models import Relative_Humidity_Events
from .models import soil_temperature_events



session = requests.Session()

def get_Device_Data(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def device_Data_Opslaan(data):
    for x in data['results']:
        serial_number = x['serial_number']
        name = x['name']
        label = x['label']
        last_seen = timezone.make_aware(timezone.datetime.strptime(x['last_seen'], '%Y-%m-%dT%H:%M:%S.%fZ'))
        last_battery_voltage = x['last_battery_voltage']
        
        try:
            #insert into data op models.py
            Device_Data.objects.create(
                serialNumber=serial_number,
                name=name,
                label=label,
                lastSeen=last_seen.date(),
                lastBatteryVoltage=last_battery_voltage
            )
        except Exception as e:
            print(f"Error: {e}")

def get_Soil_Electric_Data(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def Soil_Electric_Data(data):
    for x in data['results']:
        timestamp = x['timestamp']
        gateway_receive_time = x['gateway_receive_time']
        device = x['device']
        value = x['value']
        
        try:
            #insert into data op models.py
            Soil_Electric_Conductivity_Events.objects.create(
                timestamp=timestamp,
                gateway_receive_time=gateway_receive_time,
                device=device,
                value=value
            )
        except Exception as e:
            print(f"Error: {e}")

def get_Soil_Relative_Data(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def Soil_Relative_Data(data):
    for x in data['results']:
        timestamp = x['timestamp']
        gateway_receive_time = x['gateway_receive_time']
        device = x['device']
        value = x['value']
        
        try:
            #insert into data op models.py
            Soil_Relative_Permittivity_Events.objects.create(
                timestamp=timestamp,
                gateway_receive_time=gateway_receive_time,
                device=device,
                value=value
            )
        except Exception as e:
            print(f"Error: {e}")

def get_Battery_Data(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def Battery_Data(data):
    for x in data['results']:
        timestamp = x['timestamp']
        gateway_receive_time = x['gateway_receive_time']
        device = x['device']
        value = x['value']
        
        try:
            #insert into data op models.py
            Battery_Voltage_Events.objects.create(
                timestamp=timestamp,
                gateway_receive_time=gateway_receive_time,
                device=device,
                value=value
            )
        except Exception as e:
            print(f"Error: {e}")

def get_Par_Events_Data(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def Par_Events_Data(data):
    for x in data['results']:
        timestamp = x['timestamp']
        gateway_receive_time = x['gateway_receive_time']
        device = x['device']
        value = x['value']
        
        try:
            #insert into data op models.py
            Par_Events.objects.create(
                timestamp=timestamp,
                gateway_receive_time=gateway_receive_time,
                device=device,
                value=value
            )
        except Exception as e:
            print(f"Error: {e}")

def get_Relative_Humidity_Data(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def Relative_Humidity_Data(data):
    for x in data['results']:
        timestamp = x['timestamp']
        gateway_receive_time = x['gateway_receive_time']
        device = x['device']
        value = x['value']
        
        try:
            #insert into data op models.py
            Relative_Humidity_Events.objects.create(
                timestamp=timestamp,
                gateway_receive_time=gateway_receive_time,
                device=device,
                value=value
            )
        except Exception as e:
            print(f"Error: {e}")

def get_Soil_Temperature_Data(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def Soil_Temperature_Data(data):
    for x in data['results']:
        timestamp = x['timestamp']
        gateway_receive_time = x['gateway_receive_time']
        device = x['device']
        value = x['value']
        
        try:
            #insert into data op models.py
            soil_temperature_events.objects.create(
                timestamp=timestamp,
                gateway_receive_time=gateway_receive_time,
                device=device,
                value=value
            )
        except Exception as e:
            print(f"Error: {e}")

while True:
    deviceData = get_Device_Data("/api/devices/?format=json")
    soilElectricData = get_Soil_Electric_Data("/api/soil_electric_conductivity_events/?format=json")
    soilRelativeData = get_Soil_Relative_Data("/api/soil_relative_permittivity_events/?format=json")
    batteryData = get_Battery_Data("/api/battery_voltage_events/?format=json")
    parEventsData = get_Par_Events_Data("/api/par_events/?format=json")
    humidityData = get_Relative_Humidity_Data("/api/relative_humidity_events/?format=json")
    soilTempData = get_Soil_Temperature_Data("/api/soil_temperature_events/?format=json")

    device_Data_Opslaan(deviceData)
    Soil_Electric_Data(soilElectricData)
    Soil_Relative_Data(soilRelativeData)
    Battery_Data(batteryData)
    Par_Events_Data(parEventsData)
    Relative_Humidity_Data(humidityData)
    Soil_Temperature_Data(soilTempData)
    time.sleep(300)