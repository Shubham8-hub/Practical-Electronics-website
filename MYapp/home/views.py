from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'hometemp/index.html')

def about(request):
    return render(request, 'hometemp/about.html')
    #return HttpResponse("This is about page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        member = request.POST.get('member')
        subject = request.POST.get('subject')
        msg = request.POST.get('msg')
        contact = Contact(name=name, email=email, phone=phone, member=member, subject=subject, msg=msg, date=datetime.today())
        contact.save()
        messages.success(request, 'Your response has been recorded.')


    return render(request, 'hometemp/contact.html')

def blog(request):
    return render(request, 'hometemp/blog.html')