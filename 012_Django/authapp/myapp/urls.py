

from django.urls import path
from myapp.views import *
urlpatterns = [
    
    path("",loginpage,name="loginpage"),
    path("reg",regpage,name="regpage")
]
