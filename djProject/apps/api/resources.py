
from tastypie.resources import ModelResource
from projects.models import Project
from tasks.models import Task
from tastypie.authorization import Authorization



class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authorization = Authorization()


class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        authorization = Authorization()
