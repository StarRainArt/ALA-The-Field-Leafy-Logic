#import modules
import requests
import schedule
import time
from time import sleep
import mariadb
import datetime

#Database connectie
try:
    conn = mariadb.connect(
        user="root",
        password="edwin",
        host="localhost",
        database="sensor_data"
    )

except mariadb.Error as e:
    print(f"Error: {e}")

cur = conn.cursor()

#Lijst van alle APIS
api = 'devices'
list = [
    'battery_voltage_events',
    'par_events',
    'relative_humidity_events',
    'soil_electric_conductivity_events',
    'soil_relative_permittivity_events',
    'soil_temperature_events',
    'temperature_events'
]


class Datapoint:
    #Zorgt voor toegang API
    def __init__(self):
        self.base_url = "https://garden.inajar.nl/api/"
        self.token = "a83d911c8b57054979190015e2a3f5d823d16f56"
        self.headers = {'Authorization': f'token {self.token}',
                        'accept': 'application/json'
                        }

    #Haal voor elke API de data op die erbij hoort
    def retrieve(self):
        for uri in list:
            url = f"{self.base_url}{uri}"
            res = requests.get(url, headers=self.headers)
            print(res.text) 
            try:
                json = res.json()
            except requests.exceptions.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue  
            
            for x in json.get('results', []):  
                time.sleep(0.5)

                timestamp = x['timestamp']
                device = x['device']
                value = x['value']
                human_name = uri

                #Stuur de opgehaalde data naar de DB
                cur.execute("INSERT INTO datapoint (timestamp, device, value, human_name) VALUES (?, ?, ?, ?)",
                            (timestamp, device, value, human_name))
                conn.commit()


class DeviceData:
    #Zorgt voor toegang API
    def __init__(self):
        self.base_url = "https://garden.inajar.nl/api/"
        self.token = "a83d911c8b57054979190015e2a3f5d823d16f56"
        self.headers = {'Authorization': f'token {self.token}',
                        'accept': 'application/json'
                        }

    #Haal voor elke API de data op die erbij hoort
    def communicate(self):
        url = f"{self.base_url}{api}"
        res = requests.get(url, headers=self.headers)
        print(res.text)  
        try:
            json = res.json()
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return 

        for devices in json.get('results', []):  
            time.sleep(0.5)

            device_id = devices['id']
            serialnumber = devices['serial_number']
            name = devices['name']
            label = devices['label']
            last_seen = devices['last_seen']
            last_battery_voltage = devices['last_battery_voltage']
            human_name = api

            #Maakt normale tijd van de timestamp
            last_seen_datetime = datetime.datetime.fromtimestamp(last_seen)

            #Stuur de opgehaalde data naar de DB
            cur.execute("SELECT * FROM devicedata WHERE last_seen=? AND last_battery_voltage=?",
                        (last_seen_datetime.strftime('%Y-%m-%d %H:%M:%S'), last_battery_voltage))
            existing_data = cur.fetchone()

            if existing_data is None:
                cur.execute("INSERT INTO devicedata (device_id, serialnumber, name, label, last_seen, last_battery_voltage, human_name) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (device_id, serialnumber, name, label, last_seen_datetime.strftime('%Y-%m-%d %H:%M:%S'), last_battery_voltage, human_name))
                conn.commit()

#Roept alles aan en runt het om de 5 min
if __name__ == "__main__":
    datapoint = Datapoint()
    devicedata = DeviceData()
    # schedule.every(5).minutes.do(datapoint.retrieve)
    # schedule.every(5).minutes.do(devicedata.communicate)

    schedule.every(30).seconds.do(datapoint.retrieve)
    schedule.every(30).seconds.do(devicedata.communicate)
    while True:
        schedule.run_pending()
        sleep(1)
