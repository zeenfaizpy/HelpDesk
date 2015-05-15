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


class Address(TimestampedModel):
    """
    Model to keep track of provider contacts.
    """
    STATE_CHOICES = Choices(
        (1, 'dubai', 'Dubai'),
        (2, 'abu_dhabi', 'AbuDhabi'),
        )

    provider = models.ForeignKey(Provider,
                                 related_name="addresses")
    address_label = models.CharField(max_length=200)
    building_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    state = models.PositiveIntegerField(choices=STATE_CHOICES)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    makani = models.IntegerField(null=True, blank=True)
    contact_name = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    telephone = models.CharField(max_length=10,
                                     blank=True,
                                     validators=[
                                         RegexValidator(
                                                regex=r'^\d+$',
                                                message='Only digits are allowed'
                                                    )])
    mobile_number = models.CharField(max_length=12,
                                     blank=True,
                                     validators=[
                                         RegexValidator(
                                                regex=r'^\d+$',
                                                message='Only digits are allowed'
                                                    )])