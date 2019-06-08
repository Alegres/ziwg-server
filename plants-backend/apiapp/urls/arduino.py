from django.conf.urls import url
from apiapp.views import arduino


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',
        arduino.arduino_data, name='arduino_data'),
    url(r'^$', arduino.api_admin_arduino_index, name='api_admin_arduino_index'),
]
