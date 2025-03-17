from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def loginpage(request):
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