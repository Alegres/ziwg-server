from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', include('apiapp.urls.admin')),
    url(r'^arduino/', include('apiapp.urls.arduino')),
    url(r'^auth/', include('apiapp.urls.registration')),
    url(r'^user/', include('apiapp.urls.user')),
    url(r'^plant/', include('apiapp.urls.plant')),
    url(r'^preset/', include('apiapp.urls.preset')),
    url(r'^measurement/', include('apiapp.urls.measurement')),
    url(r'^avg_measurement/', include('apiapp.urls.avg_measurement')),
]
