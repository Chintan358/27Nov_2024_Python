from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapp.serializer import *
# Create your views here.

class CategoryAPI(APIView):

        def get(self,request):
                
                return Response("get api calling")
        
        def post(self,request):
                return Response("post api calling")

class CategoryAPIById(APIView):
        
        def get(self,request,id):
            return Response(id)
        
        def patch(self,request,id):
            return Response(id)
        
        def delete(self,request,id):
            return Response(id)
        