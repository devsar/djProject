from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'nest.views.home', name='nest_home'),

    url(r'^signup/$', 'nest.views.signup', name='nest_signup'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'nest/login.html'}, name='nest_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='nest_logout'),
    url(r'^profile$', 'nest.views.profile', name="nest_user_profile"),
)



