from django.shortcuts import render
from .models import DeviceData, DataPoint
import json

# Create your views here.

def home(request):
    unique_devices = DeviceData.objects.values('name', 'device_id').distinct()
    return render(
        request, 
        "home.html",
        {"unique_devices": unique_devices}              
    )


def dashboard(request, device_id):
    device_data = DeviceData.objects.filter(device_id=device_id)
    filtered_datapoint = DataPoint.objects.filter(device=device_id)
    unique_human_names = filtered_datapoint.values_list('human_name', flat=True).distinct()
    distinctData = DataPoint.objects.values_list('device', flat=True).distinct()

    latest_data_points = []

    name_mapping = {
        'battery_voltage_events': ('Battery Voltage', '%'),
        'soil_electric_conductivity_events': ('Soil Conductivity', 'dS/m'),
        'soil_relative_permittivity_events': ('Water Content', '%'),
        'soil_temperature_events': ('Soil Temp.', '°C'),
        'par_events': ('Light Level', 'μmol/(m²s)'),
        'relative_humidity_events': ('Humidity', '%'),
        'temperature_events': ('Temperature', '°C')
    }

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
    
    for device in distinctData:
        data_points = DataPoint.objects.filter(device=device)
        unique_names = set()
        list = []

        for data in data_points:
            human_name = data.human_name

            if human_name not in unique_names and human_name in name_mapping:
                dataApi = DataPoint.objects.filter(human_name=data.human_name, device=device).latest('timeStamp')
                readable_name = name_mapping[dataApi.human_name][0]
                unique_names.add(human_name)

                list.append({
                    "name": dataApi.human_name,
                    "value": float(dataApi.value),
                    "readableName": readable_name
                })

        deviceGroups[counter] = list
        counter = counter + 1

    validJson = json.dumps(deviceGroups)

    context = {
        'device_data': device_data,
        "filtered_datapoint": filtered_datapoint,
        "latest_values": latest_data_points,
        "json": validJson    
    }

    return render(request, "dashboard.html", context)

    

def data(request):
    datapoint = DataPoint.objects.all()
    devicedata = DeviceData.objects.all()
    sorted_reports = DeviceData.objects.order_by('-last_seen')
    # print(datapoint)
    return render(
        request, 
        "reports.html", 
        {"datapoints": datapoint, "devices": devicedata, "reports": sorted_reports}
    )

  # Fetch reports from the database sorted by arrival time
    sorted_reports = Report.objects.order_by('arrival_time')

    # Pass sorted reports to the template
    return render(request, 'report_list.html', {'reports': sorted_reports})