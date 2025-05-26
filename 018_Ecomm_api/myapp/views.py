from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from myapp.serializer import *
from myapp.models import *
# Create your views here.

class CategoryAPI(APIView):

        def get(self,request):
                
                try :
                # Fetch all categories
                    categories = Category.objects.all()
                    serializer = CategorySerializer(categories, many=True)
                    return Response(serializer.data)
                except Exception as e:
                    return Response({"error": str(e)}, status=500)     
        
        def post(self,request):
                try:
                    serializer = CategorySerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=201)
                    return Response(serializer.errors, status=400)
                except Exception as e:
                    return Response({"error": str(e)}, status=500)
               
class CategoryAPIById(APIView):
        
        def get(self,request,id):
            try:
                # Fetch a single category by ID
                category = Category.objects.get(id=id)
                serializer = CategorySerializer(category)
                return Response(serializer.data)
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=404)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
        
        def patch(self,request,id):
            try:
                # Update a category by ID
                category = Category.objects.get(id=id)
                serializer = CategorySerializer(category, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=404)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
        
        def delete(self,request,id):
            try:
                # Delete a category by ID
                category = Category.objects.get(id=id)
                category.delete()
                return Response({"message": "Category deleted successfully"}, status=204)
            except Category.DoesNotExist:
                return Response({"error": "Category not found"}, status=404)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
          
class ProductAPI(APIView):
        def get(self,request):
                try:
                    # Fetch all products
                    products = Product.objects.all()
                    serializer = ProductSerializer(products, many=True)
                    return Response(serializer.data)
                except Exception as e:
                    return Response({"error": str(e)}, status=500)     
        

class ProductAPIByCategory(APIView):
        def get(self,request,category_id):
            try:
                # Fetch products by category ID
                products = Product.objects.filter(category_id=category_id)
                serializer = ProductSerializer(products, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
        
        def post(self,request,category_id):
            try:
                # Create a new product in a specific category
                request.data['category'] = category_id
                serializer = ProductSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=201)
                return Response(serializer.errors, status=400)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
            

class ProductAPIById(APIView):
        def get(self,request,id):
            try:
                # Fetch a single product by ID
                product = Product.objects.get(id=id)
                serializer = ProductSerializer(product)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=404)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
        
        def patch(self,request,id):
            try:
                # Update a product by ID
                product = Product.objects.get(id=id)
                serializer = ProductSerializer(product, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=404)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
        
        def delete(self,request,id):
            try:
                # Delete a product by ID
                product = Product.objects.get(id=id)
                product.delete()
                return Response({"message": "Product deleted successfully"}, status=204)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=404)
            except Exception as e:
                return Response({"error": str(e)}, status=500)
