from django.shortcuts import render
from .models import DeviceData, DataPoint

# Create your views here.

def home(request):
    devicedata = DeviceData.objects.all()
    names = []  # Create an empty list to store human names
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
    return render(request, "dashboard.html")

def data(request):
    datapoint = DataPoint.objects.all()
    devicedata = DeviceData.objects.all()
    print(datapoint)
    return render(
        request, 
        "reports.html", 
        {"datapoints": datapoint, "devices": devicedata}
    )