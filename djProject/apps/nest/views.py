# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template.response import TemplateResponse


from nest.forms import SignUpForm, UserForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("projects_main"))
    return TemplateResponse(request, 'index.html', {})

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #username free, its ok to create
            form.save()
            return redirect('nest_home')
    
    data = {
        'form':form,
    }
    return TemplateResponse(request, 'nest/signup.html', data)


@login_required
def profile(request):
    user = request.user
    
    #form = UserForm(request.POST or None, instance=user)
    form = UserForm(instance=user)
    if request.method == 'POST':
        u = User.objects.get(username = request.user.username)
        form = UserForm(request.POST, instance=u)
        if form.is_valid():
            form.save()
            return redirect('nest_home')
    
    data = {
        'form':form,
    }
    
    return TemplateResponse(request, 'nest/settings.html', data)