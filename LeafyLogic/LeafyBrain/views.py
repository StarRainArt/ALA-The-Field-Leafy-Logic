from django.shortcuts import render
from .models import DeviceData, DataPoint

# Create your views here.

def home(request):
    # devicedata = DeviceData.objects.all()
    # names = [] 
    # label = []
    # for device in devicedata:
    #     names.append(device.name)
    # for labels in devicedata:
    #     label.append(labels.label)
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

    latest_values = {}

    name_mapping = {
        'battery_voltage_events': 'Battery Voltage in %',
        'soil_electric_conductivity_events': 'Soil Conductivity in dS/m',
        'soil_relative_permittivity_events': 'Water Content in %',
        'soil_temperature_events': 'Soil Temp. in °C',
        'par_events': 'Light Level in μmol/(m²s)',
        'relative_humidity_events': 'Humidity in %',
        'temperature_events': 'Temperature in °C'
    }

    for name in unique_human_names:
        latest_data_point = DataPoint.objects.filter(human_name=name).latest('timeStamp')
        latest_values[name_mapping.get(name, name)] = latest_data_point.value

    context = {
    'device_data': device_data,
    "filtered_datapoint": filtered_datapoint,
    "latest_values": latest_values
    }
    return render(
        request, 
        "dashboard.html",
        context
    )

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