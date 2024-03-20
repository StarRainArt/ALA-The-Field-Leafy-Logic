from django.shortcuts import render
from .models import DeviceData, DataPoint
from django.http import JsonResponse
from django.core import serializers

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

    deviceJson = DeviceData.objects.filter(device_id=device_id)
    device_json_data = serializers.serialize('json', deviceJson)

    dataJson = DataPoint.objects.filter(device=device_id)
    datapoint_json = serializers.serialize('json', dataJson)


    latest_data_points = []

    name_mapping = {
        'battery_voltage_events': ('Battery Voltage', '%'),
        'soil_electric_conductivity_events': ('Soil Conductivity', 'dS/m'),
        'soil_relative_permittivity_events': ('Water Content', '%'),
        'soil_temperature_events': ('Soil Temp.', '°C'),
        'par_events': ('Light Level', 'μmol/(m²s)'),
        'relative_humidity_events': ('Humidity', '%')
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

    context = {
        'device_data': device_data,
        "filtered_datapoint": filtered_datapoint,
        "latest_values": latest_data_points,
        'deviceJson': device_json_data,
        "dataPointJson": datapoint_json
        
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