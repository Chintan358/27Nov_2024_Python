from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    categoryname = models.CharField(max_length=20)
    categoryimage = models.ImageField(upload_to="categoryImage")

    def __str__(self):
        return self.categoryname


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    productname = models.CharField(max_length=20)
    price = models.IntegerField()
    qty =models.IntegerField()
    description = models.TextField()
    productimage = models.ImageField(upload_to="productImage")

    def __str__(self):
        return self.productname


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()

    #total of product price and qty
    
    def total_price(self):
        return self.product.price * self.qty



class UserAddress(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)


class UserOrder(models.Model):
    orderid = models.CharField(max_length=10,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    paymenttype = models.CharField(max_length=20)
    pid = models.CharField(max_length=50)
    address = models.ForeignKey(UserAddress,on_delete=models.CASCADE)


class OrderItems(models.Model):
    order = models.ForeignKey(UserOrder,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField()
    qty = models.IntegerField()
