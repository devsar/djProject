# -*- coding: utf-8 -*-
import logging
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

from uni_form import helpers

from nest.forms import SignUpForm, LoginForm, UserForm

def home(request):
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

def log_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        logging.error(user)
        if user and user.is_active:
            login(request,user)
            return redirect('nest_home')

    data = {
        'form':form,    
    }
    return TemplateResponse(request, 'nest/login.html', data)

def log_out(request):
    logout(request)
    return redirect('nest_home')

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

    