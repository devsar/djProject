# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from nest.forms import SignUpForm

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
