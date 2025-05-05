from django.db import models
from django.contrib.auth.models import User
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


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()

    def total_price(self):
        return self.qty*self.product.price
    
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
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.IntegerField()
    qty = models.IntegerField()


    def total_price(self):
        return self.qty*self.price
