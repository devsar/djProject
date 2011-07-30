from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'nest.views.home', name='nest_home'),
    url(r'^signup$', 'nest.views.signup', name='nest_signup'),
    url(r'^login$', 'nest.views.log_in', name='nest_login'),
    url(r'^logout$', 'nest.views.log_out', name="nest_logout"),
    url(r'^profile$', 'nest.views.profile', name="nest_user_profile"),
)



