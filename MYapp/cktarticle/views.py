from django.shortcuts import render

# Create your views here.
def easyeda(request):
    return render(request, 'cktdesart/easyeda.html')

def circuitmaker(request):
    return render(request, 'cktdesart/circuitmaker.html')