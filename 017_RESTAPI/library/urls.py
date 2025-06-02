

from django.urls import path
from library.views import *

urlpatterns = [

      path("authors", AuthorAPI.as_view()),
      path("publications",PublicationAPI.as_view()),
      path("books",BookAPI.as_view()),
      path("books/author/<int:aid>/publication/<int:pid>",addbook,name="addbook"),

      path("authorsgen",AuthorGeneric.as_view())

]
