from django.conf.urls import url
from apiapp.views import plant


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',
        plant.api_plant_detail, name='api_plant_detail'),
    url(r'^$', plant.api_admin_plant_index, name='api_admin_plant_index'),
]
