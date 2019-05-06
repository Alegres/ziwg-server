from django.conf.urls import url
from apiapp.views import preset


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$',
        preset.api_preset_detail, name='api_preset_detail'),
    url(r'^$', preset.api_admin_preset_index, name='api_admin_preset_index'),
]
