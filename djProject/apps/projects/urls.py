from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'projects.views.main', name='projects_main'),
    url(r'^project_new/$', 'projects.views.project_new', name='projects_project_new'),
    url(r'^member_add/([\d]+)/$', 'projects.views.member_add', name='projects_member_add'),
)



