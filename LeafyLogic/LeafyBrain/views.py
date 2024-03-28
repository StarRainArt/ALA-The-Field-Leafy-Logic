from django.shortcuts import render
from .models import DeviceData, DataPoint
import json

def base(request):
    devicedata = DeviceData.objects.all()
    sorted_devicedata = DeviceData.objects.latest('last_seen')
    context = {
        "time": str(sorted_devicedata)
    }
    return render(
        request, 
        "base.html",
        context
        )


#Haalt alle devicedata op waar naam en id uniek zijn en stuurt het naar home.html
def home(request):
    unique_devices = DeviceData.objects.values('name', 'device_id').distinct()
    return render(
        request, 
        "home.html",
        {"unique_devices": unique_devices}              
    )


def dashboard(request, device_id):
    #Haalt alle data op voor datapoint en devicedata, device_id word uit de URL gehaald om de juiste devicedata te krijgen
    device_data = DeviceData.objects.filter(device_id=device_id)
    filtered_datapoint = DataPoint.objects.filter(device=device_id)
    
    #Haalt weer unieke waardes op voor beide tabellen
    unique_human_names = filtered_datapoint.values_list('human_name', flat=True).distinct()
    distinctData = DataPoint.objects.values_list('device', flat=True).distinct()

    latest_data_points = []

    #Zorgt dat je betere benaming krijgt en je kan units gebruiken
    name_mapping = {
        'battery_voltage_events': ('Battery Voltage', '%'),
        'soil_electric_conductivity_events': ('Soil Conductivity', 'dS/m'),
        'soil_relative_permittivity_events': ('Water Content', '%'),
        'soil_temperature_events': ('Soil Temp.', '°C'),
        'par_events': ('Light Level', 'μmol/(m²s)'),
        'relative_humidity_events': ('Humidity', '%'),
        'temperature_events': ('Temperature', '°C')
    }

    #Haalt laatste datapoint op voor elke unique_human_name en voegt toe aan de latest_datapoints array
    for name in unique_human_names:
        latest_data_point = DataPoint.objects.filter(human_name=name).latest('timeStamp')
        if name in name_mapping:
            readable_name, unit = name_mapping[name]
        else:
            readable_name, unit = name, '' 

        latest_data_points.append({
            'name': readable_name,
            'value': latest_data_point.value,
            'unit': unit
        })

    deviceGroups = {}
    counter = 1
    
    #Zorgt voor de data waarmee de graph gemaakt kan worden
    for device in distinctData:
        #Haalt weer de juiste devicedata op en maakt alvast een object aan
        data_points = DataPoint.objects.filter(device=device)
        unique_names = set()
        list = []

        for data in data_points:
            human_name = data.human_name

            if human_name not in unique_names and human_name in name_mapping:
                #Zorgt dat je alleen de meest recente values van elke device ophaalt
                dataApi = DataPoint.objects.filter(human_name=data.human_name, device=device).latest('timeStamp')
                deviceTitles = DeviceData.objects.filter(device_id=dataApi.device).values('name').latest('last_seen')
                #geeft weer een betere benaming
                readable_name = name_mapping[dataApi.human_name][0]
                unique_names.add(human_name)
                
                #Data wordt toegevoegd aan de list
                list.append({
                    "name": dataApi.human_name,
                    "value": float(dataApi.value),
                    "readableName": readable_name,
                    "device": deviceTitles['name']
                })

        #Geeft de array een naam
        deviceGroups[counter] = list
        counter = counter + 1

    #Json word gemaakt
    validJson = json.dumps(deviceGroups)

    context = {
        'device_data': device_data,
        "filtered_datapoint": filtered_datapoint,
        "latest_values": latest_data_points,
        "json": validJson    
    }

    #Stuurt data naar dashboard
    return render(request, "dashboard.html", context)

    
#Haalt allemaal data op en stuurt het naar reports.html
def data(request):
    datapoint = DataPoint.objects.all()
    devicedata = DeviceData.objects.all()
    sorted_reports = DeviceData.objects.order_by('-last_seen')
    return render(
        request, 
        "reports.html", 
        {"datapoints": datapoint, "devices": devicedata, "reports": sorted_reports}
    )