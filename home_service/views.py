from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
import datetime

# Create your views here.
def notification():
    status = Status.objects.get(status='pending')
    new = Service_Man.objects.filter(status=status)
    count=0
    for i in new:
        count+=1
    d = {'count':count,'new':new}
    return d


def Home(request):
    return render(request,'home.html')

def contact(request):
    error=False
    if request.method=="POST":
        n = request.POST['name']
        e = request.POST['email']
        m = request.POST['message']
        status = Status.objects.get(status="unread")
        Contact.objects.create(status=status,name=n,email=e,message1=m)
        error=True
    d = {'error':error}
    return render(request,'contact.html',d)

def about(request):
    return render(request,'about.html')

def Login_User(request):
    error = ""
    d = {'error': error}
    return render(request, 'login.html', d)

def Login_admin(request):
    error = ""
    d = {'error': error}
    return render(request, 'admin_login.html', d)

def Signup_User(request):
    error = ""
    d = {'error':error}
    return render(request,'signup.html',d)

def All_Service(request):
    return render(request,'services.html')

def search_cities(request):
    return render(request,'search_cities.html')
