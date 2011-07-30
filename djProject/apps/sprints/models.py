
from django.db import models
from django.utils.translation import ugettext as _

from projects.models import Project

SPRINT_STATUS = (
    ('active', _("Active")),
    ('archived', _("Archived")),
)


class Sprint(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=32)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choice=SPRINT_STATUS)

class TimeLog(models.Model):
    sprint = models.ForeignKey(Sprint)
    start_time = models.DateTimeField()
    hours = models.DecimalField()
    description = models.TextField()

    
    
