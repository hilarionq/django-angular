# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 15:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='business_hours_end',
            field=models.IntegerField(default=17, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)]),
        ),
    ]
