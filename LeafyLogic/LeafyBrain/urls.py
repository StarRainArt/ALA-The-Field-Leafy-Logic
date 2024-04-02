from django.urls import path
from . import views

#Specificeert alle URLS
urlpatterns = [
    path("", views.home, name="home"),
    path("reports/", views.data, name="reports"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('dashboard/<int:device_id>/', views.dashboard, name='dashboard')
]