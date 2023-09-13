from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        phonenumber=request.POST['phno']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password1']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username alreary Exists")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already Exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1,email=email)
                user.save()

                print("user created")
                return redirect('login')


        else:
            messages.info(request, "password not matching")
            return redirect('register')

    return render(request, "register.html")


def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('credentials:rlogin')

    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
