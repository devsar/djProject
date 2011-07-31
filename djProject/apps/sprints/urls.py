from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^new/(?P<project_id>[\d]+)/$', 'sprints.views.sprint_new', name='sprints_new'),
)



