from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.


def dashboard(request):
    return render(request, 'base.html')
    


def register(request):
    return render(request, 'register.html')


def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        owner = request.POST['owner']
        manager = request.POST['manager']

        if owner == 'on':
            owner = True
        else:
            owner = False
        if manager == 'on':
            manager = True
        else: 
            manager = False
        user = CustomUser.objects.create(email=email, password=password, owner=owner, manager=manager)
        user.save()
        return redirect('login')
    else:
        return render(request, 'register.html')



def login(request):
    return render(request, 'login.html')



def login_user(request):
    if request.method == 'POST':
        print('post request')
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            print('user is not none')
            login(request)
            return redirect('dashboard')
        return HttpResponse('user is none')
    return HttpResponse('not post request')

