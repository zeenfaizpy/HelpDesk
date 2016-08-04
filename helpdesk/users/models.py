# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models


class User(AbstractUser):
    """
    Model to keep registred user data.
    """
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    mobile_number = models.CharField(max_length=12,
                                     blank=True,
                                     validators=[
                                         RegexValidator(
                                                regex=r'^\d+$',
                                                message='Only digits are allowed'
                                                    )])

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
