from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view,APIView
from myapp.models import *
from myapp.serilizer import *
from rest_framework.response import Response

@api_view(['get'])
def getStudents(request):
    allstudents = Student.objects.all()
    ser =  StudentSerializer(allstudents, many=True)
    return Response({"data":ser.data})

@api_view(['post'])
def addstudent(request):
    ser =  StudentSerializer(data = request.data)
    if not ser.is_valid():
        return Response({"error":ser.errors,"message":"Something went Wrong"})
    
    ser.save()
    return Response({"data":ser.data,"message":"Data inserted successfully !!!"})

@api_view(['delete'])
def deletestudent(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return Response({"message":"Student deleted !!!"})


@api_view(['put'])
def updatestudent(request,id):
    student = Student.objects.get(pk=id)
    ser =  StudentSerializer(student, request.data)
    if not ser.is_valid():
        return Response({"error":ser.errors,"message":"Something went Wrong"})
    
    ser.save()
    return Response({"data":ser.data,"message":"Data updated successfully !!!"})
    
@api_view(['patch'])
def updatepstudent(request,id):
    student = Student.objects.get(pk=id)
    ser =  StudentSerializer(student, request.data,partial=True)
    if not ser.is_valid():
        return Response({"error":ser.errors,"message":"Something went Wrong"})
    
    ser.save()
    return Response({"data":ser.data,"message":"Data updated successfully !!!"})


class BookAPI(APIView):

    def get(self,request):
        allbook = Book.objects.all()
        ser = BookSerialize(allbook,many=True)
        return Response({"data":ser.data})
    

    def post(self,request):
        ser = BookSerialize(data = request.data)
        if not ser.is_valid():
            return Response({"error":ser.errors,"message":"Something went Wrong"})
    
        ser.save()
        return Response({"data":ser.data,"message":"Book inserted successfully !!!"})

    def put(self,request):
        book = Book.objects.get(pk=request.data['id'])
        ser =  BookSerialize(book, request.data)
        if not ser.is_valid():
             return Response({"error":ser.errors,"message":"Something went Wrong"})
    
        ser.save()
        return Response({"data":ser.data,"message":"Book updated successfully !!!"})



    def delete(self,request):
        book = Book.objects.get(pk=request.data['id'])
        book.delete()
        return Response({"message":"Book deleted succesfully"})

    
