
from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("contact",contact,name="contact"),
    path("details",details,name="details"),
    path("shop",shop,name="shop"),
]