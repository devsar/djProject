from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'projects.views.main', name='projects_main'),
    url(r'^project_new/$', 'projects.views.project_new', name='projects_project_new'),
)



