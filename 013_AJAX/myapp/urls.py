


from django.urls import path
from myapp.views import *
urlpatterns = [
    path("",index,name="index"),
    path("test",test,name="test"),
    path("country",country,name="country"),
    path("state",state,name="state"),
    path("city",city,name="city")

]
