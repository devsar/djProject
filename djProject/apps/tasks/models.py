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

class Task:
    label = models.CharField(max_length=255)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User)
    spend = models.FloatField(default=0)
    parent = models.ForeignKey('self')
    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES)
    sprint = models.ForeignKey(Sprint, null=True, blank=True)
    
class Tag:
    label = models.CharField(max_length=255)
    task = models.ForeignKey(Task)
    
class Log:
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    task = models.ForeignKey(Task)
    description = models.CharField(max_length=255)
    
    
    
