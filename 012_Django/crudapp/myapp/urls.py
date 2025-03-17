


from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path("",index,name="index"),
    path("adduser",adduser,name="adduser"),
    path("display",display,name="display"),
    path('delete/<id>',deleteuser,name="delete"),
    path('update/<id>',userbyid,name="update"),
    path('updateuser',updateuser,name="updateuser")
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
