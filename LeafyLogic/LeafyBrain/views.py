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
    unique_name = DeviceData.objects.values('name').distinct()
    return render(
        request, 
        "home.html",
        {"device_names": unique_name}              
    )


def dashboard(request):
    devicedata = DataPoint.objects.all()
    human_names = [] 
    for device in devicedata:
        human_names.append(device.human_name)
    return render(
        request, 
        "dashboard.html",
        {"human_name": human_names}              
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