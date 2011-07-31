from django.contrib import admin
from tasks.models import Task, Comment

admin.site.register(Comment)
admin.site.register(Task)

