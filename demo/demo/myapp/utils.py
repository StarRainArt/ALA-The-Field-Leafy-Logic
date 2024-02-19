import requests
import time
from django.utils import timezone
from .models import Device_Data

session = requests.Session()

def get_Device_Data(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def device_Data_Opslaan(devices):
    for x in devices['results']:
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

def Soil_Electric_Data(devices):
    for x in devices['results']:
        timestamp = x['timestamp']
        gateway_receive_time = x['gateway_receive_time']
        device = x['device']
        value = x['value']
        
        try:
            #insert into data op models.py
            Device_Data.objects.create(
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
    
    device_Data_Opslaan(deviceData)
    Soil_Electric_Data(soilElectricData)
    time.sleep(300)