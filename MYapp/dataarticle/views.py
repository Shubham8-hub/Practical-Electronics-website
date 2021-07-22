from django.shortcuts import render

# Create your views here.
def ic555(request):
    return render(request, 'dataart/ic555.html')


def cd4017(request):
    return render(request, 'dataart/cd4017.html')