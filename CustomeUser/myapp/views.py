from django.shortcuts import render,HttpResponse
# from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()


def index(request):

    user = User(phone_number="1452639685",info="sttff user",is_staff=True)
    user.set_password("123")
    user.save()

    return HttpResponse("user created")
