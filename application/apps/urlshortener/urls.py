from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^view/(?P<slug>\w+)$', views.ShortURLView.as_view(), name='view_short_url'),
    url(r'^(?P<slug>\w+)/stats$', views.ShortURLStatsView.as_view(), name='short_url_redirect_stats'),
    url(r'^(?P<slug>\w+)$', views.ShortURLRedirectView.as_view(), name='short_url_redirect'),
    url(r'^$', views.ShortURLCreateView.as_view(), name='create_short_url'),
)