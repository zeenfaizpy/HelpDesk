# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('address_label', models.CharField(max_length=200)),
                ('building_name', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=200)),
                ('state', models.PositiveIntegerField(choices=[(1, b'Dubai'), (2, b'AbuDhabi')])),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('makani', models.IntegerField(null=True, blank=True)),
                ('contact_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\d+$', message=b'Only digits are allowed')])),
                ('mobile_number', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(regex=b'^\\d+$', message=b'Only digits are allowed')])),
                ('provider', models.ForeignKey(related_name='addresses', to='providers.Provider')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
