from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djProject.views.home', name='home'),
    url(r'^', include('nest.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^sprints/', include('sprints.urls')),
    url(r'^tasks/', include('tasks.urls')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
