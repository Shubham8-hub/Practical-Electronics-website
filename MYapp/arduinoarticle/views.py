# This is views.py of adruino article

from django.shortcuts import render

# Create your views here.
def blink(request):
    return render(request, 'adruinoart/blink.html')

def ultrasonic(request):
    return render(request, 'adruinoart/ultrasonic.html')