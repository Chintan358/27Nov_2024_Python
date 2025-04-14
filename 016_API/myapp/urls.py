
from django.urls import path
from myapp.views import *

urlpatterns = [
    
    path("",index,name="index"),
    path("sendmail",sendmail,name="sendmail"),
    path("payment",payment,name="payment"),
    path("pay",pay,name="pay")
]
