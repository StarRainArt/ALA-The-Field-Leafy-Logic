import requests
import mariadb
import time

conn = mariadb.connect(
    user="root",
    password="edwin",
    host="localhost",
    database="sensor_data")
cur = conn.cursor() 

session = requests.Session()

def dataOphalen(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

def dataVersturen(devices):

    for x in devices['results']:

        serial_number = x['serial_number']
        name = x['name']
        label = x['label']
        last_seen = x['last_seen']
        last_battery_voltage = x['last_battery_voltage']
        
        try: 
            cur.execute("INSERT INTO device_data (serial_number, name, label, last_seen, last_battery_voltage) VALUES (?, ?, ?, ?, ?)", (serial_number, name, label, last_seen, last_battery_voltage))
            conn.commit()
        except mariadb.Error as e: 
            print(f"Error: {e}")

    cur.execute("SELECT serial_number, name FROM device_data")

    for serial_number, name in cur: 
        print(f" Name: {name}, Serial Number: {serial_number}")

while True:
    devices = dataOphalen("/api/devices/?format=json")

    dataVersturen(devices)
    time.sleep(300)