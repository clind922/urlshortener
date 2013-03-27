from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('application.apps.urlshortener.urls', namespace='urlshortener')),
)

urlpatterns += staticfiles_urlpatterns()
