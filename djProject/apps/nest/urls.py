from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'nest.views.home', name='nest_home'),
    url(r'^signup$', 'nest.views.signup', name='nest_signup'),
   
)



