import requests
import mariadb

conn = mariadb.connect(
    user="root",
    password="edwin",
    host="localhost",
    database="sensor_data")
cur = conn.cursor() 

# myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
# myUrl =  'https://garden.inajar.nl/api/devices/?format=json'
# head = {'Authorization': 'token {}'.format(myToken)}

# r = requests.get(myUrl, headers=head)

session = requests.Session()

# def split_database(text):
    # with open("database.txt", "r") as f:
    #     lines = f.readlines()


#    info = text.split(" | ")
#    device = info[0]
#    time = info[1]
#    temperature = info[2]

#    print(device + '\n' + time)

# split_database("Device748181 | 4841914941 | 48")

def dataOphalen(uri):
    myToken = 'a83d911c8b57054979190015e2a3f5d823d16f56'
    myUrl =  f'https://garden.inajar.nl{uri}'
    head = {'Authorization': 'token {}'.format(myToken)}
    r = session.get(myUrl, headers=head)
    return r.json()

# print(dataOphalen("/api/battery_voltage_events/?format=json"))
devices = dataOphalen("/api/devices/?format=json")

# print(devices['results'][1])

for x in devices['results']:

    serial_number = x['serial_number']
    name = x['name']
    label = x['label']
    last_seen = x['last_seen']
    last_battery_voltage = x['last_battery_voltage']
    
    #insert information 
    try: 
        cur.execute("INSERT INTO device_data (serial_number, name, label, last_seen, last_battery_voltage) VALUES (?, ?, ?, ?, ?)", (serial_number, name, label, last_seen, last_battery_voltage))
        conn.commit()
    except mariadb.Error as e: 
        print(f"Error: {e}")

#retrieving information 
cur.execute("SELECT serial_number, name FROM device_data") #WHERE first_name=?", (some_name,))

for device, battery_voltage in cur: 
    print(f"Name: {name}, Serial Number: {serial_number}")