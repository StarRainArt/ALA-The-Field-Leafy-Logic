from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request, "home.html")

