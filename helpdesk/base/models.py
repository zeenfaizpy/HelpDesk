#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class TimeAuditModel(models.Model):
    """
    Common model to save created date and last modified date.
    """
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserAditModel(models.Model):
    """
    Common model to save created user and last modified user.
    """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="created_%(class)s_related",
                                   null=True,
                                   blank=True)
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                         related_name="updated_%(class)s_related",
                                         null=True,
                                         blank=True)

    class Meta:
        abstract = True


class AuditModel(TimeAuditModel, UserAditModel):
    """
    """
    class Meta:
        abstract = True