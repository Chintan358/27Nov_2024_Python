from django.shortcuts import render,redirect
from myapp.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def adduser(request):
    if request.method=='POST':
        data = request.POST
        username = data.get('uname')
        email = data.get('email')
        age=data.get("age")

        User.objects.create(username=username,email=email,age=age)
        # user = User(username=username,email=email,age=age)
        # user.save()
        messages.add_message(request, messages.SUCCESS, "Registration success")
        return render(request,'index.html')

def display(request):
    users  = User.objects.all()
    return render(request,"display.html",{"users":users})

def deleteuser(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect("display")

def userbyid(request,id):
    user = User.objects.get(pk=id)
    return render(request,'update.html',{"user":user})

def updateuser(request):
     if request.method=='POST':
        data = request.POST
        id = data.get("id")
        username = data.get('uname')
        email = data.get('email')
        age=data.get("age")

        user = User.objects.get(pk=id)
        user.username=username
        user.email=  email
        user.age = age
        user.save()
       
        messages.add_message(request, messages.SUCCESS, "update success")
        # return render(request,'update.html')
        return redirect("display")