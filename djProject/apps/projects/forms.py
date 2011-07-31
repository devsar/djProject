from django import forms
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User 
from projects.models import Member

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=100, label=_("Name"))


class ProjectMemberForm(forms.Form):
    users = forms.ModelMultipleChoiceField(User.objects.all())
