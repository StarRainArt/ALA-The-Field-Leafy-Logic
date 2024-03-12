from django.shortcuts import render
from .models import DeviceData, DataPoint

# Create your views here.

def home(request):
    devicedata = DeviceData.objects.all()
    names = [] 
    label = []
    for device in devicedata:
        names.append(device.name)
    for labels in devicedata:
        label.append(labels.label)
    return render(
        request, 
        "home.html",
        {"names": names, "labels": label}              
    )

def reports(request):
    return render(request, "reports.html")


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
    print(datapoint)
    return render(
        request, 
        "reports.html", 
        {"datapoints": datapoint, "devices": devicedata}
    )