from django import forms
from django.utils.translation import ugettext as _
from sprints.models import Sprint



class SprintForm(forms.ModelForm):
    #name = forms.CharField(max_length=100, label=_("Name"))
    class Meta:
        model = Sprint
        exclude = ["project"]

        
