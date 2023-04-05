from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers

from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView )

urlpatterns = [
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('authentication.urls')),
    path('api/', include('api.urls')),
    path('generator/', include('generator.urls')),
    path('admin/', admin.site.urls),
]
