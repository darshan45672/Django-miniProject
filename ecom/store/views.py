from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm, UpdatePasswordForm, UserInfoForm
from django.contrib.auth.models import User
from django.db.models import Q

def categorySummary(request):
    categories = Category.objects.all()
    return render(request, 'categorySummary.html', {"categories": categories})

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
            messages.success(request,("You have registered Sucessfully, fill you info"))
            return redirect('updateInfo')
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
    
def updateUser(request):
    if request.user.is_authenticated:
        currentUser = User.objects.get(id=request.user.id)
        userForm = UpdateUserForm(request.POST or None, instance = currentUser)

        if userForm.is_valid():
            userForm.save()
            login(request, currentUser)
            messages.success(request,("User has been updated"))

            return redirect('home')
        return render(request, 'userUpdate.html', {'userForm': userForm})
    else:
        messages.success(request,("You need to be logged in to update your profile"))
        return redirect('login')
    
def updatePassword(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = UpdatePasswordForm(current_user, request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been updated")
                # login(request, current_user)
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        else:
            form = UpdatePasswordForm(current_user)
            return render(request, 'userPassword.html', {"form" : form})
    else:
        messages.success(request,("You need to be logged in to update your password"))
        return redirect('login')
    
def updateInfo(request):
    if request.user.is_authenticated:
        currentUser = Profile.objects.get(user__id=request.user.id)
        userInfoForm = UserInfoForm(request.POST or None, instance = currentUser)

        if userInfoForm.is_valid():
            userInfoForm.save()
            messages.success(request,("User Info has been updated"))
            return redirect('home')
        
        return render(request, 'updateInfo.html', {'userInfoForm': userInfoForm})
    else:
        messages.success(request,("You need to be logged in to update your profile"))
        return redirect('login')
    
def search(request):
    if request.method == "POST":
        searchItem = request.POST['search']
        searchedItem = Product.objects.filter(Q(name__icontains=searchItem) | Q(description__icontains=searchItem))
        if not searchedItem:
            messages.success(request,("No search results found"))
            return render(request, 'search.html', {})   
        return render(request, 'search.html', {'searchItem': searchedItem})   
    
    else:
        return render(request, 'search.html', {})