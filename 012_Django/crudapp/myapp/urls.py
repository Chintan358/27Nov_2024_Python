


from django.urls import path
from myapp.views import *

urlpatterns = [
    
    path("",index,name="index"),
    path("adduser",adduser,name="adduser"),
    path("display",display,name="display"),
    path('delete/<id>',deleteuser,name="delete"),
    path('update/<id>',userbyid,name="update"),
    path('updateuser',updateuser,name="updateuser")
]
