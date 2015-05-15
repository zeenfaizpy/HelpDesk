from django.contrib import admin

from .models import (ServiceKeyword, Service, Provider,
    Address)

admin.site.register(ServiceKeyword)
admin.site.register(Service)
admin.site.register(Provider)
admin.site.register(Address)