from django.shortcuts import render
from rest_framework.decorators import APIView
from library.models import *
from library.serializer import *
from rest_framework.response import Response
# Create your views here.


class AuthorAPI(APIView) : 
    def get(self, request):
        try :
            allAuthors = Author.objects.all()
            ser = AuthorSerializer(allAuthors,many=True)
            return Response({"Data":ser.data,"status":"200"})
        except Exception as e :
            return Response({"message":"Somthing went wrong","Errors":e})

    def post(self,request):
        
        try :
            ser = AuthorSerializer(data = request.data)
            if not ser.is_valid():
                return Response({"message":"something went wrong","Errors":ser.errors})
            
            ser.save()
            return Response({"message":"success","status":"201","data":ser.data})

        except Exception as e :
            print("errr")
            return Response({"message":"Somthing went wrong","Errors":e})
        
    def put(self,request):
        try :
            author = Author.objects.get(pk=request.data['id'])
            ser = AuthorSerializer(author, request.data)
            if not ser.is_valid():
                return Response({"message":"something went wrong","Errors":ser.errors})
            
            ser.save()
            return Response({"message":"success","status":"201","data":ser.data})

        except Exception as e :
            print("errr")
            return Response({"message":"Somthing went wrong","Errors":e})

    def delete(self,request):
        try :
            author = Author.objects.get(pk=request.data['id'])
            author.delete()
            return Response({"message":"success"})

        except Exception as e :
            print("errr")
            return Response({"message":"Somthing went wrong","Errors":e})
        

class PublicationAPI(APIView):
    def get(self, request):
        try :
            allpub = Publication.objects.all()
            ser = PublicationSerializer(allpub,many=True)
            return Response({"Data":ser.data,"status":"200"})
        except Exception as e :
            return Response({"message":"Somthing went wrong","Errors":e})

    def post(self,request):
        
        try :
            ser = PublicationSerializer(data = request.data)
            if not ser.is_valid():
                return Response({"message":"something went wrong","Errors":ser.errors})
            
            ser.save()
            return Response({"message":"success","status":"201","data":ser.data})

        except Exception as e :
            print("errr")
            return Response({"message":"Somthing went wrong","Errors":e})
        
    def put(self,request):
        try :
            pub = Publication.objects.get(pk=request.data['id'])
            ser = PublicationSerializer(pub, request.data)
            if not ser.is_valid():
                return Response({"message":"something went wrong","Errors":ser.errors})
            
            ser.save()
            return Response({"message":"success","status":"201","data":ser.data})

        except Exception as e :
            print("errr")
            return Response({"message":"Somthing went wrong","Errors":e})

    def delete(self,request):
        try :
            author = Publication.objects.get(pk=request.data['id'])
            author.delete()
            return Response({"message":"success"})

        except Exception as e :
            print("errr")
            return Response({"message":"Somthing went wrong","Errors":e})
        
