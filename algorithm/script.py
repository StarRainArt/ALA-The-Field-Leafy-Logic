import requests

class Datapoint:
    def __init__(self):
        self.base_url = "https://garden.inajar.nl/api/relative_humidity_events"
        self.token = "a83d911c8b57054979190015e2a3f5d823d16f56"
        self.headers = {'Authorization': f'token {self.token}', 'accept': 'application/json'}

    def fetch_data(self):
        response = requests.get(self.base_url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

    def control_water(self, data):
        if not data:
            print("No data available.")
            return
        
        for entry in data['results']:
            device_id = entry['device']
            water_content = entry['value']
            
            if water_content > 60:  # If water content is too high
                print(f"Turning off water for device {device_id}")
                # Code to turn off water for the device goes here
            elif water_content < 40:  # If water content is too low
                print(f"Turning on water for device {device_id}")
                # Code to turn on water for the device goes here
            else:
                print(f"Ideal water content for device {device_id}")
                # No action needed, water content is within desired range

# Create an instance of the Datapoint class
datapoint = Datapoint()

# Fetch data
data = datapoint.fetch_data()

# Control water based on the fetched data
datapoint.control_water(data)
