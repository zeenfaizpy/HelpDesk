from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

from model_utils import Choices

from helpers.models import TimestampedModel


class ServiceKeyword(TimestampedModel):
    """
    Model to keep track of service keywords.
    """
    name = models.CharField(max_length=300)

class Service(TimestampedModel):
    """
    Model to keep track of service.
    """
    name = models.CharField(max_length=300)
    keywords = models.ManyToManyField(ServiceKeyword,
                                      related_name="services")

class Provider(TimestampedModel):
    """
    Model to keep track of solution provider details.
    """
    TYPE_CHOICES = Choices(
        (1, 'individual', 'Individual'),
        (2, 'company', 'Company'),
        )

    name = models.CharField(max_length=300)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='provider',
                                blank=False)
    type = models.PositiveIntegerField(choices=TYPE_CHOICES)
    services = models.ManyToManyField(Service,
                                      related_name="providers")


