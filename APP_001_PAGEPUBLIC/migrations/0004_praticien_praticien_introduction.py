# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-29 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_001_PAGEPUBLIC', '0003_auto_20180829_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='praticien',
            name='praticien_introduction',
            field=models.TextField(blank=True, null=True),
        ),
    ]
