

from django.urls import path
from library.views import *

urlpatterns = [

      path("authors", AuthorAPI.as_view()),
      path("publications",PublicationAPI.as_view())

]
