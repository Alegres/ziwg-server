from django.conf.urls import url
from apiapp.views import plantDelete


urlpatterns = [
url(r'^(?P<pk>[0-9]+)/$',   plantDelete.api_plant_delete, name='api_plant_delete'),
 ]