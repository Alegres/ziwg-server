"""apiskeleton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from apiapp.serializers.token import CustomJWTSerializer


jwtpatterns = [
    url(r'^jwt/refresh-token/', refresh_jwt_token, name='refresh_jwt_token'),
    url(r'^jwt/api-token-verify/', verify_jwt_token, name='verify_jwt_token'),
    url(r'^jwt/api-token-auth/', ObtainJSONWebToken.as_view(
        serializer_class=CustomJWTSerializer), name='obtain_jwt_token'),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apiapp.urls')),
] + jwtpatterns