from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['get'])
def getStudents(request):
    return HttpResponse("get api calling")

@api_view(['post'])
def addstudent(request):
    return HttpResponse("post api calling")

@api_view(['delete'])
def deletestudent(request):
    return HttpResponse("delete api calling")


@api_view(['put'])
def updatestudent(request):
    return HttpResponse("put api calling")