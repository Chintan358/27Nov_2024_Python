from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
# Create your views here.
def index(request):

    allcategories = Category.objects.all()
    allproducts = Product.objects.all()
    return render(request,"index.html",{"categories":allcategories,"products":allproducts})

@login_required(login_url="loginregister")
def accounts(request):
    return render(request,"accounts.html")

@login_required(login_url="loginregister")
def cart(request):
    return render(request,"cart.html")

@login_required(login_url="loginregister")
def checkout(request):
    return render(request,"checkout.html")

def details(request):
    return render(request,"details.html")

def shop(request):
    return render(request,"shop.html")

def loginregister(request):
    return render(request,"login-register.html")


def registeruser(request):
    if request.method=="POST":
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password=data.get("password")

        if User.objects.filter(username=username).exists():
            return render(request,'login-register.html',{'err':"Username exist !!!"})

        user = User(username=username,email=email)
        user.set_password(password)
        user.save()

        return render(request,'login-register.html',{'msg':"Registration success !!!"})
    

def loginuser(request):
    if request.method=="POST":
        data = request.POST
        username = data.get("username")
        password=data.get("password")

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("index")
        
        else:
            return render(request,'login-register.html',{'loginerr':"Invalid Credentials !!!"})


@login_required(login_url="loginregister")
def logoutuser(request):
    logout(request)
    return redirect("index")