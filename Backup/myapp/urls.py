
from django.urls import path
from myapp.views import *

urlpatterns = [
   path('', index, name='index'),  # Home page
   path('payment', payment, name='payment'),  # Payment page
]
