from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = User.objects.filter(username=username)
        if users.count() > 0:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    return render(request, 'auth-login.html')


def LogoutView(request):
    logout(request)
    return redirect('login')


def Register(request):
    return render(request, 'auth-forgot-password.html')
