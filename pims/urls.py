from django.conf.urls import patterns, url, include
from django.contrib import admin

from backend import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pontos/$', views.PontoView.as_view()),
    #url(r'^valores/(?P<pk>[0-9]+)/$', 'tipo_detail'),
)

#urlpatterns = format_suffix_patterns(urlpatterns)