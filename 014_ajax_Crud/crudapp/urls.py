
from django.urls import path
from crudapp.views import *

urlpatterns = [
    
    path("",index,name="index"),
    path('display',display,name="display"),
    path("addstudent",addstudent,name="addstudent"),
    path("deletestudent",deletestudent,name="deletestudent"),
    path('studentbyid',studentbyid,name="studentbyid"),
    path("editstudent",editstudent,name="editstudent"),
    path("search",search,name="search")
]
