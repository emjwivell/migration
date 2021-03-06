# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 18:20
from __future__ import unicode_literals

from django.db import migrations


def read_data():
    with open("/Users/emilywivell/PycharmProjects/Django_Migrations/text.txt") as infile:
        data = infile.readlines()
        return [line.replace('\n', '').split(',') for line in data]


def load_data(apps, schema_editor):
    stats = read_data()
    Sport = apps.get_model("django_migrate", "SportsSchema")
    for row in stats:
        Sport.objects.create(name=row[0], att=row[1], yds=row[2], avg=row[3], long=row[4], td=row[5])


class Migration(migrations.Migration):

    dependencies = [
        ('django_migrate', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
