from django.conf.urls import patterns, include, url
from teams.views import Home, Season, Money, Month

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'homerun_pool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^season/$', Season.as_view(), name='season'),
    url(r'^money/$', Money.as_view(), name='money'),
    url(r'^(?P<month>(April|May|June|July|August|September))/$', Month.as_view(), name='month'),

    url(r'^admin/', include(admin.site.urls)),
)
