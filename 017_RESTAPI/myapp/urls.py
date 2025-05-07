from django.urls import path
from myapp.views import *

urlpatterns = [

        path("students",getStudents,name="students"),
        path("addstudent",addstudent,name="addstudent"),
        path("deletestudent",deletestudent,name="deletestudent"),
        path("updatestudent",updatestudent,name="updatestudent")

]
