from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=20)

class State(models.Model):
    name = models.CharField(max_length=20)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=20)
    state=models.ForeignKey(State,on_delete=models.CASCADE)

    