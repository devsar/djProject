# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from uni_form import helpers

class SignUpForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and password.
    """
    username = forms.RegexField(label=_("Username"), max_length=30, regex=r'^[\w.@+-]+$',
        help_text = ("Required. 30 characters or fewer. Letters, digits and @/./+/-/ only."),
        error_messages = {'invalid': ("This value may contain only letters, numbers and @/./+/-/ characters.")}
    )
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput,
        help_text = _("Enter the same password as above, for verification.")
    )

    class Meta:
        model = User
        fields = ("username","email")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_("A user with that username already exists."))

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError(_("The two password fields didn't match."))
        return password2
   
    def clean_mail(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(_("E-mail Already taken."))

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
#    @property
#    def helper(self):
#        """ We call this as a method/property so we don't make the form helper a singleton. """
#        # instantiate the form helper object
#        helper = helpers.FormHelper()
#
#        # add in some input controls (a.k.a. buttons)
#        submit = helpers.Submit('submit','Submit')
#        helper.add_input(submit)
#
#        # define the form action
#        helper.form_action = reverse('nest_signup')
#        helper.form_method = 'POST'
#        #helper.form_class = ''
#        #helper.form_id = 'nest_signup'
#        return helper

class LoginForm(forms.ModelForm):
    username = forms.CharField(label=_("Username"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput) 
    class Meta:
        model = User
        fields = ('username','password')   
        
    @property
    def helper(self):
        """ We call this as a method/property so we don't make the form helper a singleton. """

        # instantiate the form helper object
        helper = helpers.FormHelper()

        # add in some input controls (a.k.a. buttons)
        submit = helpers.Submit('submit','Log In')
        helper.add_input(submit)

        # define the form action
        helper.form_action = reverse('nest_login')
        helper.form_method = 'POST'
        #helper.form_class = ''
        #helper.form_id = 'nest_signup'
        return helper    