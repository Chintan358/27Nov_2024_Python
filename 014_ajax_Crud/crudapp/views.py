from django.shortcuts import render,HttpResponse
from crudapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def display(request):
    allStduents = Student.objects.all()
    return JsonResponse({"data":list(allStduents.values())})

def addstudent(request):
    if request.method=='POST':
        uname = request.POST['uname']
        email = request.POST['email']
        age = request.POST['age']

        Student.objects.create(username=uname,email=email,age=age)

    return HttpResponse("Student Inserted !!!!")

def deletestudent(request):
    sid = request.GET['sid']
    std =  Student.objects.get(pk=sid)
    std.delete()
    return HttpResponse("Student Deleted !!!")


def studentbyid(request):
    sid = request.GET['sid']
    std =  Student.objects.filter(pk=sid)
    return JsonResponse({"data":list(std.values())})

def editstudent(request):
    std =Student.objects.get(pk=request.POST['id'])
    std.username = request.POST['uname']
    std.email = request.POST['email']
    std.age = request.POST['age']
    std.save()
    return HttpResponse("Student updated !!!!")

def search(request):
    value = request.GET['value']
    allStduents =  Student.objects.filter(username__startswith=value)
    return JsonResponse({"data":list(allStduents.values())})