from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Publication(models.Model):
    name  = models.CharField(max_length=20)
    address = models.TextField()


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication = models.ForeignKey(Publication,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    qty = models.IntegerField()

