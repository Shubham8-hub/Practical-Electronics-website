#This is blogs veiws.py

from django.shortcuts import render, HttpResponse

# Create your views here.
def dataSheet(request):
    return render(request, 'blogtemp/datas.html')

def Adruino(request):
    return render(request, 'blogtemp/adrun.html')

def circuitdesign(request):
    return render(request, 'blogtemp/ckt.html')