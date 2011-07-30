
from tastypie.resources import ModelResource
from projects.models import Project
from tasks.models import Task
from tastypie.authorization import Authorization



class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authorization = Authorization()

    def get_object_list(self, request):
        
        projects = super(ProjectResource, self).get_object_list(request)        
        return projects.filter(member__user=request.user)


class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        authorization = Authorization()

    def get_object_list(self, request):        
        tasks = super(TaskResource, self).get_object_list(request)        
        return tasks.filter(project__member__user=request.user)
