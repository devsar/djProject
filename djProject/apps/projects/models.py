import logging

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

import pusher

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
    
    def save(self, *args , ** kwargs ):
        super(Project, self).save(* args, ** kwargs)
        try:
            pusher.app_id = '6417'
            pusher.key = '93d0509ce62dd993b05a'
            pusher.secret = 'c824cb5eb3b9c96f863b'           
            
            p = pusher.Pusher()
            for user in User.objects.all():
                p[user.username].trigger('new_project', {
                    'project': self.to_dict()
                })
        except:
            logging.exception("error notifying")

class Member(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    role = models.CharField(choices=USER_ROLES, max_length=12)

