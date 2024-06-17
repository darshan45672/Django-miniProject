from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
# from django import forms

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

def registerUser(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data['username']
            userPassword = form.cleaned_data['password1']

            # authenticate and log in user
            user = authenticate(username = userName, password= userPassword)
            login(request, user)
            messages.success(request,("You have registered Sucessfully"))
            return redirect('home')
        else:
            messages.success(request,("cant register.........."))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})
    
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product' : product})

def category(request, categorySearch):
    categorySearch = categorySearch.replace('-',' ')
    # category from url
    try:
        # search category
        getCategory = Category.objects.get(name=categorySearch)
        product = Product.objects.filter(category= getCategory)
        return render(request, 'category.html', {'products': product, 'category': getCategory})
    except:
        messages.success(request,("The category is unavailable"))
        return redirect('home')