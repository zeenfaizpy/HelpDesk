from django.db import models


class TimestampedModel(models.Model):
    """
    Helper model to save created date and last modified date.
    """
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
