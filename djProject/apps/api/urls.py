from django.conf.urls.defaults import patterns, include, url

from api.resources import ProjectResource, TaskResource

project_resource = ProjectResource()
task_resource = TaskResource()

urlpatterns = patterns('',
     (r'^v1/', include(project_resource.urls)),
     (r'^v1/', include(task_resource.urls)),
)



