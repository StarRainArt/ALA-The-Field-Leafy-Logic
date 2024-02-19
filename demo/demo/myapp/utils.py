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
            #insert into device_data op models.py
            Device_Data.objects.create(
                serialNumber=serial_number,
                name=name,
                label=label,
                lastSeen=last_seen.date(),
                lastBatteryVoltage=last_battery_voltage
            )
        except Exception as e:
            print(f"Error: {e}")

while True:
    devices = get_Device_Data("/api/devices/?format=json")
    device_Data_Opslaan(devices)
    time.sleep(300)