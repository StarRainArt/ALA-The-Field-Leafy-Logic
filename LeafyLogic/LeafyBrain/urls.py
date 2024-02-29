from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reports", views.reports, name="reports"),
    path("dashboard", views.dashboard, name="dashboard")
]