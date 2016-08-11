#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.base_user import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from django_countries.fields import CountryField

from .managers import UserManager


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model with email as username.
    """
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)

    is_staff = models.BooleanField(default=False,
        help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField(default=True,
        help_text='Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField(default=timezone.now)

    mailing_address = models.TextField(blank=False, default='')
    current_location = CountryField(null=True)
    current_city = models.CharField(max_length=120, blank=False, default='')
    mobile_number = models.CharField(max_length=20, blank=False, default='')
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['email']


    def full_name(self):
        return u'%s %s' % (self.first_name.strip(), self.last_name.strip())

    def get_short_name(self):
        return u'%s' % (self.first_name.strip())

    def __unicode__(self):
        return self.full_name
