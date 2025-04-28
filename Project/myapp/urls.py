
from django.urls import path
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path("",index,name="index"),
    path("accounts",accounts,name="accounts"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("details",details,name="details"),
    path("shop",shop,name="shop"),
    path("loginregister",loginregister,name="loginregister"),

    path("registeruser",registeruser,name="registeruser"),
    path("loginuser",loginuser,name="loginuser"),
    path("logoutuser",logoutuser,name="logoutuser"),
    path("addtocart",addtocart,name="addtocart"),
    path("removecart",removecart,name="removecart"),
    path("changeqty",changeqty,name="changeqty"),
    path("addadr",addadr,name="addadr"),
    path("viewadr",viewadr,name="viewadr")


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)