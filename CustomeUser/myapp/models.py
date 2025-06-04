from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomeUser(AbstractUser):

    username=None
    phone_number = models.CharField(max_length=15,unique=True)
    info = models.CharField(max_length=100)

    USERNAME_FIELD= 'phone_number'
    REQUIRED_FIELDS =[]
    objects = UserManager()


    

@receiver(post_save, sender=CustomeUser)
def create_user_object(sender, instance, **kwargs):
    print("user created")
    print(sender,instance)