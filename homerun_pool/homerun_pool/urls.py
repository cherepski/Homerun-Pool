from django.conf.urls import patterns, include, url
from teams.views import Home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homerun_pool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
