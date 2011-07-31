from django import forms
from django.utils.translation import ugettext as _



class ProjectForm(forms.Form):
    name = forms.CharField(max_length=100, label=_("Name"))
