from django.conf.urls import url
from apiapp.views import measurement


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',
        measurement.api_measurement, name='api_measurement'),
    url(r'^$', measurement.api_admin_measurement_index, name='api_admin_measurement_index'),
]
