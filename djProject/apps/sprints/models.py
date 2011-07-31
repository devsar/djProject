
from django.db import models
from django.utils.translation import ugettext as _

from projects.models import Project
from nest.utils import get_pusher
import logging

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

    def save(self, *args , ** kwargs ):
        if self.id is None:
            message = 'sprint_created'
        else:
            message = 'sprint_updated'
            
        super(Sprint, self).save(* args, ** kwargs)
            
        try:
            p = get_pusher()
            for member in self.project.member_set.all():
                p[member.user.username].trigger(message, {
                    'sprint':  {'id': self.id, 'project': self.project.id}
                })
        except:
            logging.exception("error notifying")
        
        
class TimeLog(models.Model):
    sprint = models.ForeignKey(Sprint)
    start_time = models.DateTimeField()
    hours = models.DecimalField(decimal_places=2, max_digits=4)
    description = models.TextField()

    
    
