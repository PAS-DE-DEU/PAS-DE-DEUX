from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth import login, logout, authenticate
from .models import *

# Create your views here.

@never_cache
def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if Account.objects.filter(email=email).exists():
                messages.info(request,'Email already registered. Please log in.')
                return redirect('signup')
            elif Account.objects.filter(phone_number=phone_number).exists():
                messages.info(request, 'Phone number already registered. Please log in.')
                return redirect('signup')
            else:
                user = Account.objects.create_user(first_name=first_name,last_name=last_name,phone_number=phone_number, email=email, password=password)
                user.is_active = True
                user.save()
                print(user.first_name)
                login(request, user)
                return redirect('home')
        else:
             messages.info(request, 'Invalid Entry')
             return redirect('signup')
    return render(request, 'auth/SignUp.html')

@never_cache
def UserLogin(request):
    if request.user.is_authenticated:
            return redirect('home')
    else:
         if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                if Account.objects.filter(is_active = False):
                    messages.info(request, 'Your Account has been Suspended')
                    return redirect('login')
                else:
                    messages.error(request, 'Invalid Username or Password')
                    return redirect('login')
    return render(request, 'auth/Login.html')

@never_cache
def UserLogout(request):
    logout(request)
    return redirect('home')