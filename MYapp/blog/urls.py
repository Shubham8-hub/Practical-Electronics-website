# This is created urls.py for blogs

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("dataSheet", views.dataSheet, name='dataSheet'),
    path("Adruino", views.Adruino, name='Adruino'),
    path("circuit-design", views.circuitdesign, name='circuitdesign'),
]