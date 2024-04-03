from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product


# Create your views here.

def allproducts(request, slug_c=None):
    page_c = None
    products = None
    if slug_c != None:
        page_c = get_object_or_404(Category, slug=slug_c)
        products = Product.objects.all().filter(category=page_c, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    return render(request, 'home.html', {'category': page_c, 'products': products})

def prod_det(request, slug_c, slug_p):
    try:
        product = Product.objects.get(category__slug=slug_c, slug=slug_p)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})

def home(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = name
        myuser.last_name = lname
        myuser.save()

        return redirect('signin')
    return render(request, 'signup.html')




def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request, 'invalid password or username')

            return redirect('signin')
    else:
        return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('allproducts')


def account(request):
    return render(request, 'account.html')


def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('allproducts')
    else:
        # Handle GET requests, maybe render a confirmation page
        return render(request, 'delete.html')






