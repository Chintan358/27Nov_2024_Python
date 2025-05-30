
from django.urls import path
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

        path("users",registeruser,name="users"),
        path("categories",CategoryAPI.as_view()),
        path("categories/<int:id>",CategoryAPIById.as_view()),
        path("products",ProductAPI.as_view()),
        path("products/category/<int:category_id>",ProductAPIByCategory.as_view()),
        path("products/<int:id>",ProductAPIById.as_view()),   
        # path('api-token-auth/', views.obtain_auth_token),    
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)