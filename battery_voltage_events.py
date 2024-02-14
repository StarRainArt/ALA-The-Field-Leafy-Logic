import requests
import db
import time

class Battery_voltage_events:
    def __init__(self, base_url, token):
        self.session = requests.Session()
        self.base_url = base_url
        self.headers = {'Authorization': f'token {token}'}

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
    token = "a83d911c8b57054979190015e2a3f5d823d16f56"
    base_url = "https://garden.inajar.nl"
    manager = Battery_voltage_events(base_url, token)
    manager.run()

        

