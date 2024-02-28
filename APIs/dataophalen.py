import requests
import schedule
from time import sleep
import mariadb

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

list = [
    'battery_voltage_events',
    'par_events',
    'relative_humidity_events',
    'soil_electric_conductivity_events',
    'soil_relative_permittivity_events',
    'soil_temperature_events'
]

class Datapoint:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://garden.inajar.nl/api/"
        self.token = "a83d911c8b57054979190015e2a3f5d823d16f56"
        self.headers = {'Authorization': f'token {self.token}',
                        'accept': 'application/json'
                        }

    def retrieve(self, uri):
        url = f"{self.base_url}{uri}/"
        response = requests.get(url, headers=self.headers)
        # print(response) #.json()
        x = response.json()['results']
        timestamp = x['timestamp']
        device = x['device']
        value = x['value']
        human_name = uri

        cur.execute("INSERT INTO datapoint (timestamp, device, value, human_name) VALUES (?, ?, ?, ?)", (timestamp, device, value, human_name))
        conn.commit()

    def run(self):
        for x in list:
            self.retrieve(x)



if __name__ == "__main__":
    datapoint = Datapoint()
    # schedule.every(5).minutes.do(datapoint.run)
    schedule.every(5).seconds.do(datapoint.run)
    while True:
        schedule.run_pending()
        sleep(1)


