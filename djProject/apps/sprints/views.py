# Create your views here.
from sprints.forms import SprintForm
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from projects.models import Project


@login_required
def sprint_new(request, project_id):
    """
        add new project
    """
    project = get_object_or_404(Project, id=project_id)
    form = SprintForm(request.POST or None, initial={'start_date': '2011-07-30', 'end_date': '2011-07-31'})
    if form.is_valid():
        sprint = form.save(commit=False)
        sprint.project = project
        sprint.save()

        return HttpResponse("Sprint Created!")
    return TemplateResponse(request, "sprints/sprint_new.html", {'form': form}) 