# This is created urls.py for data articles

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("ic555", views.ic555, name='ic555'),
    path("cd4017", views.cd4017, name='cd4017'),
]