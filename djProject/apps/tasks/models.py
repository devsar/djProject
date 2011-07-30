from django.db import models
from django.contrib.auth.models import User

from sprints.models import *

STATUS_CHOICES = (
    ('O','Open'),
    ('C','Closed'),
    ('P', 'In Progress'),
    ('B','Blocked'),
)

PRIORITY_CHOICES = (
    ('1','High'),
    ('2','Medium'),
    ('3','Low')
    
)

class Task(models.Model):
    project = models.ForeignKey(Project)
    sprint = models.ForeignKey(Sprint, null=True, blank=True)
    owner = models.ForeignKey(User, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    estimated = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    spend = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    remaining = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES)
    
    
    
class Tag(models.Model):
    label = models.CharField(max_length=255)
    task = models.ForeignKey(Task)
    
class Log(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task)
    description = models.CharField(max_length=255)
    
    
    
