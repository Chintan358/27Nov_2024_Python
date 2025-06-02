from django.shortcuts import render
from rest_framework.decorators import APIView,api_view
from library.models import *
from library.serializer import *
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics

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
        

class BookAPI(APIView):
    def get(self, request):
        try :
            allbooks = Book.objects.all()
            ser = BookSerializer(allbooks,many=True)
            return Response({"Data":ser.data,"status":"200"})
        except Exception as e :
            return Response({"message":"Somthing went wrong","Errors":e})
        
    # def post(self,request):
    #     try :
    #         ser = BookSerializer(data = request.data)   
    #         if not ser.is_valid():
    #             return Response({"message":"something went wrong","Errors":ser.errors})
    #         ser.save()
    #         return Response({"message":"success","status":"201","data":ser.data})
    #     except Exception as e :
    #         print("errr")
    #         return Response({"message":"Somthing went wrong","Errors":e})

    # def put(self,request):
    #     try :
    #         book = Book.objects.get(pk=request.data['id'])
    #         ser = BookSerializer(book, request.data)
    #         if not ser.is_valid():
    #             return Response({"message":"something went wrong","Errors":ser.errors})
            
    #         ser.save()
    #         return Response({"message":"success","status":"201","data":ser.data})

    #     except Exception as e :
    #         print("errr")
    #         return Response({"message":"Somthing went wrong","Errors":e})
    def delete(self,request):
        try :
            book = Book.objects.get(pk=request.data['id'])  
            book.delete()
            return Response({"message":"success"})
        except Exception as e :
            print("errr")
            return Response({"message":"Somthing went wrong","Errors":e})
        

@api_view(['POST'])
def addbook(requset, aid, pid):
    try:
        author = Author.objects.get(pk=aid)
        publication = Publication.objects.get(pk=pid)

        requset.data.update({"author": author.id})
        requset.data.update({"publication": publication.id})
        if requset.method == "POST":
            ser = BookSerializer(data=requset.data)
            if not ser.is_valid():
                return Response({"message": "something went wrong", "Errors": ser.errors})
            ser.save()
            return Response({"message": "success", "status": "201", "data": ser.data})
    except Exception as e:
        print("errr")
        return Response({"message": "Somthing went wrong", "Errors": e})
   


class AuthorGeneric(generics.ListCreateAPIView):
    queryset  = Author.objects.all()
    serializer_class=AuthorSerializer
   