import requests
import time
import schedule
import db

uriList = [
    "par_events",
    "battery_voltage_events",
    "relative_humidity_events",
    "soil_electric_conductivity_events",
    "soil_relative_permittivity_events",
    "soil_temperature_events"
]

class Device:
    def __init__(self):
        self.base_url = "https://garden.inajar.nl/api/"
        self.token = "a83d911c8b57054979190015e2a3f5d823d16f56"
        self.headers = {'Authorization': f'token {self.token}'}

    def communicate(self):
        for x in uriList:
            url = f"{self.base_url}{x}"
            response = requests.get(url, headers=self.headers)
            json = response.json()
               
            for y in json['results']:
                time.sleep(0.5)

                timestamp = y['timestamp']
                device = y['device']
                value = y['value']

                db.cur.execute(f"INSERT INTO datapoint (timestamp, device, value, human_name) VALUES (?, ?, ?, ?)", (timestamp, device, value, x))
                db.conn.commit()

                
if __name__ == "__main__":
    device = Device()
    # schedule.every(5).minutes.do(datapoint.run)
    schedule.every(5).seconds.do(device.communicate)
    while True:
        schedule.run_pending()
        time.sleep(1)