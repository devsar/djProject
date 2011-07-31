
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS

from projects.models import Project
from tasks.models import Task


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
        filtering = {
            'project': ALL_WITH_RELATIONS,
            'sprint': ALL_WITH_RELATIONS,
            'description': ALL,
        }

    def get_object_list(self, request):        
        tasks = super(TaskResource, self).get_object_list(request)        
        return tasks.filter(project__member__user=request.user)

    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(TaskResource, self).build_filters(filters)

        if "project" in filters:
            orm_filters["project__id"] = filters['project']
        if "sprint" in filters:
            orm_filters["sprint__id"] = filters['sprint']
        
        return orm_filters
