from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'base.html')
    else:
        return redirect('login')



def register(request):
    return render(request, 'register.html')


def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        owner = request.POST.get('owner') == 'on'
        manager = request.POST.get('manager') == 'on'

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            owner=owner,
            manager=manager,
        )
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
            auth_login(request, user)
            print('logged in')
            # redirect to dashboard page 
            return redirect('dashboard')
        return redirect('login')
    return redirect('login')


def logout_user(request):
    logout(request)
    return redirect('login')