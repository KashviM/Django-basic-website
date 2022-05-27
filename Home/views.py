from datetime import datetime
from email import message
from multiprocessing import context
from tkinter import Variable
from django.shortcuts import render,HttpResponse

from Home.models import Contact
from django.contrib import messages



# Create your views here.
def index(request):
    # return HttpResponse("This is Homepage")
    # context={
    #       'variable':' HELLOOOO VARIABLE WORLD ',
    #       'variable2':' HELLOOOO VARIABLE2 innnnnn WORLD '
    # }
    # messages.success(request,'this is test message')
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, phone=phone,email=email,desc=desc)
        contact.save()
        messages.success(request, 'Form has been submitted successful')
    return render(request,'contact.html')



