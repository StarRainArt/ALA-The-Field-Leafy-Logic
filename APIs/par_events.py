import requests
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
import db
import db
import time

class Par_events:
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
            timestamp = x['timestamp']
            device = x['device']
            value = x['value']

            db.cur.execute("INSERT INTO par_events (timestamp, device, value) VALUES (%s, %s, %s)", (timestamp, device, value))
            db.conn.commit()

    def run(self):
        while True:
            device = self.retrieve('/api/par_events/?format=json')
            self.send(device)
            time.sleep(300)

if __name__ == "__main__":
    manager = Par_events()
    manager.run()

        

