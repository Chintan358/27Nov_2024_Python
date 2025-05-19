
from django.urls import path
from myapp.views import *
urlpatterns = [

        path("categories",CategoryAPI.as_view()),
        path("categories/<int:id>",CategoryAPIById.as_view())

        
]
