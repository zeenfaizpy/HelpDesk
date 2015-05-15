from django import forms
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm

from crispy_forms.helper import FormHelper

from .models import UserProfile

class LoginForm(AuthenticationForm):
    """
    make use of authentication form for login.
    """
    def __init__(self, *args, **kwargs):
        """
        Overriding to enable crispy forms.
        """
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False


class ChangePasswordForm(SetPasswordForm):
    """
    A form that let's user change password without entering old password.
    """
    def __init__(self, *args, **kwargs):
        """
        Enabling crispy forms.
        """
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.form_tag = False