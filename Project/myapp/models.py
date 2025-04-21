from django.db import models

# Create your models here.
class Category(models.Model):
    categoryname = models.CharField(max_length=20)
    categoryimage = models.ImageField(upload_to="categoryImage")

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    productname = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()
    description=models.TextField()
    productImage=models.ImageField(upload_to="productImage")    