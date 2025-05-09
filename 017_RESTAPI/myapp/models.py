from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    age = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()
    