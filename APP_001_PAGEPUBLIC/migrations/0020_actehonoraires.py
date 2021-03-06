# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-18 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_001_PAGEPUBLIC', '0019_acte'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActeHonoraires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actehonoraires_titre', models.CharField(max_length=120, verbose_name='Acte')),
                ('actehonoraires_duree', models.CharField(blank=True, max_length=120, null=True, verbose_name="Durée de l'acte")),
                ('actehonoraires_type', models.CharField(blank=True, max_length=120, null=True, verbose_name='Cabinet/visite')),
                ('actehonoraires_honoraire', models.CharField(blank=True, max_length=120, null=True, verbose_name='Honoraire')),
                ('actehonoraires_cpam', models.CharField(blank=True, max_length=120, null=True, verbose_name='Remboursement CPAM')),
            ],
            options={
                'verbose_name_plural': 'Honoraire',
            },
        ),
    ]
