from django.urls import path
from myapp.views import *
urlpatterns = [

    path("create",index,name="index")
]