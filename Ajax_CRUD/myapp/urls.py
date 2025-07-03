

from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("display",display,name="display"),
    path("register",register,name="register")
]
