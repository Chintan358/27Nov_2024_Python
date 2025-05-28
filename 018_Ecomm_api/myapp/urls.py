
from django.urls import path
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
urlpatterns = [

        path("users",registeruser,name="users"),
        path("categories",CategoryAPI.as_view()),
        path("categories/<int:id>",CategoryAPIById.as_view()),
        path("products",ProductAPI.as_view()),
        path("products/category/<int:category_id>",ProductAPIByCategory.as_view()),
        path("products/<int:id>",ProductAPIById.as_view()),   
        path('api-token-auth/', views.obtain_auth_token),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)