from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 


from projects.forms import ProjectForm, ProjectMemberForm  
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
def member_add(request, id_project):
    project = get_object_or_404(Project, id=id_project)
    form = ProjectMemberForm(request.POST or None)
    if form.is_valid():
        users = form.cleaned_data['users']
        for user in users:
            try:
                Member.objects.filter(project=project, user=user).get()
            except Member.DoesNotExist:
                Member(user=user, project=project, role='leader').save()
        return HttpResponse("Member Saved!")
    return TemplateResponse(request, "projects/member_add.html", {'form': form}) 
    
