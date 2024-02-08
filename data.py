import requests
import json
import db
import time

session = requests.Session()

def retrieveData(uri):
    token = "a83d911c8b57054979190015e2a3f5d823d16f56"
    url = f"https://garden.inajar.nl{uri}"
    head = {'Authorization': 'token {}'.format(token)}

    res = session.get(url, headers=head)

    return res.json()


def send(devices):
    for x in devices['results']:
        serial_number = x['serial_number']
        name = x['name']
        label = x['label']
        last_seen = x['last_seen']
        battery = x['last_battery_voltage']

        db.cur.execute("INSERT INTO device_data (serial_number, name, label, last_seen, last_battery_voltage) VALUES (%s, %s, %s, %s, %s)", (serial_number, name, label, last_seen, battery))
        db.conn.commit()

while True:
    devices = retrieveData('/api/devices/?format=json')

    send(devices)
    time.sleep(300)  # 300sec / 5min

