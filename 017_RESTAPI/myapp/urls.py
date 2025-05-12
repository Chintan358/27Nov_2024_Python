from django.urls import path
from myapp.views import *

urlpatterns = [

        path("students",getStudents,name="students"),
        path("addstudent",addstudent,name="addstudent"),
        path("deletestudent/<id>",deletestudent,name="deletestudent"),
        path("updatestudent/<id>",updatestudent,name="updatestudent"),
        path("updatepstudent/<id>",updatepstudent,name="updatepstudent"),

        path("books",BookAPI.as_view())

]
