from django.shortcuts import render,HttpResponse
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"index.html")


def display(request):
    students = Student.objects.all()

    return JsonResponse({"students":list(students.values())})

def register(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']

        Student.objects.create(name=name,email=email,phone=phone,age=age)

        return HttpResponse("registration success")