
from tastypie.resources import ModelResource
from projects.models import Project


class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'


class TaskResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'task'
