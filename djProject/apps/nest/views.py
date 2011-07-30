# -*- coding: utf-8 -*-
import logging
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse

from uni_form import helpers

from nest.forms import SignUpForm, LoginForm

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

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = form['username']
        password = form['password']
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                return redirect('nest_home')
    
    data = {
        'form':form,    
    }
    return TemplateResponse(request, 'nest/login.html', data)