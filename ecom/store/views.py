from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products' : products})

def about(request):
    return render(request, 'about.html', {})

def loginUser(request):
    if request.method == "POST":
        userName = request.POST['username']
        userPassword = request.POST['password']

        user = authenticate(request, username = userName, password = userPassword )

        if user is not None:
            login(request, user)
            messages.success(request, ("you have logged in"))
            return redirect('home')
        else: 
            messages.success(request, ("there was a error man........."))
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})

def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been Logged out"))
    return redirect('home')