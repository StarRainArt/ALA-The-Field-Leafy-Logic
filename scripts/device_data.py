import requests
import time
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
import db

class Device_data:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://garden.inajar.nl"
        self.token = "a83d911c8b57054979190015e2a3f5d823d16f56"
        self.headers = {'Authorization': f'token {self.token}'}

    def retrieve(self, uri):
        url = f"{self.base_url}{uri}"
        response = self.session.get(url, headers=self.headers)
        return response.json()
    
    def send(self, device):
        for x in device['results']:
            serial_number = x['serial_number']
            name = x['name']
            label = x['label']
            last_seen = x['last_seen']
            battery = x['last_battery_voltage']

            db.cur.execute("INSERT INTO device_data (serial_number, name, label, last_seen, last_battery_voltage) VALUES (%s, %s, %s, %s, %s)", (serial_number, name, label, last_seen, battery))
            db.conn.commit()

    def run(self):
        while True:
            device = self.retrieve('/api/devices/?format=json')
            self.send(device)
            time.sleep(300)

if __name__ == "__main__":
    manager = Device_data()
    manager.run()

        

