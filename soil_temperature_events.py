import requests
import db
import time

class Soil_temperature_events:
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
            timestamp = x['timestamp']
            device = x['device']
            value = x['value']

            db.cur.execute("INSERT INTO soil_temperature_events (timestamp, device, value) VALUES (%s, %s, %s)", (timestamp, device, value))
            db.conn.commit()

    def run(self):
        while True:
            device = self.retrieve('/api/soil_temperature_events/?format=json')
            self.send(device)
            time.sleep(300)

if __name__ == "__main__":
    token = "a83d911c8b57054979190015e2a3f5d823d16f56"
    base_url = "https://garden.inajar.nl"
    manager = Soil_temperature_events(base_url, token)
    manager.run()

        

