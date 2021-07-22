# This is created urls.py for circuit design article

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("easyeda", views.easyeda, name='easyeda'),
    path("circuitmaker", views.circuitmaker, name='circuitmaker'),
]