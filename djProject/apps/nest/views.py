# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.template.response import TemplateResponse

from nest.forms import SignUpForm 

def home(request):
    return TemplateResponse(request, 'index.html', {})

def signup(request):
    data = {}
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                User.objects.get(username = form.username)
                data.update({'error':'User already taken.'})
            except User.DoesNotExist:
                #username free, its ok to create
                form.save()
    
    data.update(
        {'form':form}
    )
    return TemplateResponse(request, 'nest/signup.html', data)