# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-08-30 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_001_PAGEPUBLIC', '0013_auto_20180830_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabinet',
            name='cabinet_lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Cabinet latitude'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='cabinet_lng',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Cabinet longitude'),
        ),
    ]
