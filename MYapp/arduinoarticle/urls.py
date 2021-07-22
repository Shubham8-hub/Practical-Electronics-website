# This is created urls.py for adruino article

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("blink", views.blink, name='blink'),
    path("ultrasonic", views.ultrasonic, name='ultrasonic'),
]