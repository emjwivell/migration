# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_migrate', '0003_sportsschema_joels_fave_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sportsschema',
            name='joels_fave_field',
        ),
    ]
