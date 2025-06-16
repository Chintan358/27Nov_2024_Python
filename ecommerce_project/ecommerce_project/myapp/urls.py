from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path("",index,name="index"),
    path("cart",cart,name="cart"),
    path("checkout",checkout,name="checkout"),
    path("contact",contact,name="contact"),
    path("detail",detail,name="detail"),
    path("shop",shop,name="shop"),
    path("register",register_page,name="register"),
    path("login",login_page,name="login"),
    path("logout",logout_page,name="logout"),

    path("api/products", getProdducts, name="product-list"),
    path("api/categories", getCategories, name="category-list"),

    path("add-to-cart", add_to_cart, name="add_to_cart"),


    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)