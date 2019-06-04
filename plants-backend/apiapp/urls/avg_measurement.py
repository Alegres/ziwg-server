from django.conf.urls import url
from apiapp.views import avg_measurement


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',
        avg_measurement.api_avg_measurement, name='api_avg_measurement'),
    url(r'^$', avg_measurement.api_admin_avg_measurement_index, name='api_admin_avg_measurement_index'),
]
