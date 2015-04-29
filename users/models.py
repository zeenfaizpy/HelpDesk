from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse_lazy
from django.conf import settings


class UserProfile(AbstractUser):
    """
    Model to store details of users.
    """
    mobile_number = models.CharField(max_length=12,
                                     blank=True,
                                     validators=[
                                         RegexValidator(
                                                regex=r'^\d+$',
                                                message='Only digits are allowed'
                                                    )])

    class Meta:
        pass
    
    @property                              
    def full_name(self):
        """
        Return combined firstname and lastname, otherwise return username.
        This can be used in template so that a real name will be shown if first
        name and last name is filled, otherwise username will be shown.
        """
        if self.first_name or self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return self.username

    def __unicode__(self):
        """
        Show the object in a readable way.
        """
        return self.full_name()
