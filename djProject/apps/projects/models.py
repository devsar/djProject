import datetime 
from dateutil.relativedelta import *

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


PROJECT_STATUS = (
    ('active', _("Active")),
    ('closed', _("Finish")),
    ('archived', _("Archived")),
)

USER_ROLES = (
    ('leader', _("Leader")),
    ('developer', _("Developer")),
    ('client', _("Client")),
)

class Project(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=32)
    since = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=PROJECT_STATUS, max_length=12)
    feed = models.URLField(max_length=512, null=True, blank=True)
    
    #TODO: transaction here
    def new(self, creator, name):
        """
            create a new projects, this add membership and add default sprints  
        """
        from sprints.models import Sprint
        self.name = name
        self.creator = creator
        self.status = 'active'
        #TODO: add feed url
        self.save()
          
        member = Member()
        member.new(creator, self, 'leader')
        
        sprint = Sprint()
        start_date = datetime.datetime.now()
        end_date = start_date + relativedelta(weeks=1)
        sprint.new(self, 'Sprint', start_date, end_date)
        
        return self
        
    

class Member(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    role = models.CharField(choices=USER_ROLES, max_length=12)

    def new(self, user, project, role):
        self.user = user
        self.project = project
        self.role = role
        self.save()
        
        
        
