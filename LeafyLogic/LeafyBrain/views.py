from django.shortcuts import render
from .models import DeviceData, DataPoint

# Create your views here.
def home(request):
    return render(request, "home.html")

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