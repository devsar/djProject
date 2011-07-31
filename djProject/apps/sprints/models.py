
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
    status = models.CharField(choices=SPRINT_STATUS, max_length=12)
    
    def new(self, project, name, start_date, end_date):
        self.project = project
        self.name = name
        self.status = 'active'
        self.start_date = start_date
        self.end_date = end_date 
        self.save()
        return self
    
    def __unicode__(self):
        return u"%s" % self.name
                
        
        
class TimeLog(models.Model):
    sprint = models.ForeignKey(Sprint)
    start_time = models.DateTimeField()
    hours = models.DecimalField(decimal_places=2, max_digits=4)
    description = models.TextField()

    
    
