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
    status = models.CharField(choices=PROJECT_STATUS)
    feed = models.URLField(max_length=512)

class Member(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    role = models.CharField(choices=USER_ROLES)

