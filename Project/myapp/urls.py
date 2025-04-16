
from django.urls import path
from myapp.views import *

urlpatterns = [
  
    path("",index,name="index"),
    path("accounts",accounts,name="accounts"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("details",details,name="details"),
    path("shop",shop,name="shop"),
    path("loginregister",loginregister,name="loginregister"),

]
