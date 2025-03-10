from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()


    