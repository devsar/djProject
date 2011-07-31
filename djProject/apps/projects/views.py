from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404 


from projects.forms import ProjectForm  
from projects.models import Project, Member

@login_required
def main(request):
    membership = Member.objects.filter(user=request.user)
    return TemplateResponse(request, 
                            "projects/main.html", 
                            {'membership': membership})

    
@login_required
def project_new(request):
    """
        add new project
    """
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        creator = request.user
        project = Project()
        project.new(creator, name)
        return HttpResponse("Project Created!")
    return TemplateResponse(request, "projects/project_new.html", {'form': form}) 
        

@login_required
def project_edit(request, id_project):
    pass


@login_required
def task_new(request):
    pass


@login_required
def task_edit(request, id_project):
    pass