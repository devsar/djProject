from django.conf.urls.defaults import patterns, include, url

from api.resources import ProjectResource, TaskResource, SprintResource

project_resource = ProjectResource()
sprint_resource = SprintResource()
task_resource = TaskResource()

urlpatterns = patterns('',
     (r'^v1/', include(project_resource.urls)),
     (r'^v1/', include(sprint_resource.urls)),
     (r'^v1/', include(task_resource.urls)),
)



