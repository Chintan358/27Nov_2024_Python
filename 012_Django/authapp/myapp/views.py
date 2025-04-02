from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def loginpage(request):
    if request.method=='POST':
        uname = request.POST['uname']
        password = request.POST['pass']

        if not User.objects.filter(username=uname).exists():
            messages.add_message(request, messages.ERROR, "Invalid credentials !!!")
            return render(request,"login.html")

        user = authenticate(username=uname,password=password)

        if user is not None:
             login(request,user)
             return render(request,"home.html")
        else:
            messages.add_message(request, messages.ERROR, "Invalid credentials !!!")
            return render(request,"login.html")


    return render(request,"login.html")

def regpage(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        password = request.POST['pass']

        if User.objects.filter(username=uname).exists():
            messages.add_message(request, messages.ERROR, "Username alredy Exists !!!")
            return render(request,"reg.html")

        user = User(first_name=fname,last_name=lname,username=uname)
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "Registration successful !!!")
        return render(request,"reg.html")

    return render(request,"reg.html")

def logoutuser(request):
    logout(request)
    return render(request,"login.html")


@login_required(login_url="loginpage")
def home(request):
    return render(request,"home.html")