from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('userena.urls')),
    (r'^$', 'teams.views.homePage'),
    (r'^submissions/', 'teams.views.submissions'),
    (r'^problem/(\d{1,2})/', 'teams.views.problem'),
    (r'^scoreboard', 'teams.views.scoreboard'),
)
