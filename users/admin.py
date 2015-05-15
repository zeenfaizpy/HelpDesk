from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm 
from django import forms

from .models import UserProfile

class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserProfile


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class UserProfileAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile_number',)}),
    )

admin.site.site_header = 'HelpDesk Administration'
admin.site.site_title = 'HelpDesk'
admin.site.index_title = 'HelpDesk Apps'

admin.site.register(UserProfile, UserProfileAdmin)