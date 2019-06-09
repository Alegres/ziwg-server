from django.conf.urls import url
from apiapp.views import registration


urlpatterns = [
    url(r'^login/', registration.api_login, name='api_login'),
    url(r'^register/', registration.api_register, name='api_register'),
    url(r'^user/', registration.api_user_detail, name='api_user_detail'),
    url(r'^password/', registration.api_password_change, name='api_password_change'),
]
