from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.
def home(request):
    details = Event_Details.objects.filter(status='Publish')

    context = {
        'details' : details,
    }

    return render(request,'home.html',context)

def EventDescription(request,id):
    details = Event_Details.objects.filter(id=id).first()

    context = {
        'x' : details,
    }
    return render(request,'event_desc.html',context)

# -----------------------------------------------------------
# search
def search(request):
    query = request.GET.get('query')
    event = Event_Details.objects.filter(name__icontains = query)
    context = {
        'event': event,
    }
    return render(request,'search.html',context)

# --------------------------------------------------------------

# Contact us Page
def contact(request):
    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')

       x = Contact_Page(
            name = name,
            email = email,
            message = message,
        )
       x.save()
       return redirect('home')

    return render(request,'contact.html',{})

# --------------------------------------------------------------

# About us Page
def about(request):
    return render(request,'about.html',{})

# --------------------------------------------------------------
# Authentication

# user registration
def User_Register(request):
    if request.method=="POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username, email, pass1)
        customer.first_name = first_name 
        customer.last_name = last_name 
        customer.save()
        return redirect('User_Login')

    return render(request,'Auth/register.html',{})


# --------------------------------------------------------------


# login
def User_Login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('User_Login')

        
    
    return render(request,'Auth/register.html',{})

# --------------------------------------------------------------


# logout
def User_Logout(request):
    logout(request)
    return redirect('home')


# --------------------------------------------------------------


# cart
@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Event_Details.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Event_Details.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Event_Details.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Event_Details.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    return render(request, 'cart.html')