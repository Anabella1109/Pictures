# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citacione', '0006_remove_location_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='place',
            field=models.CharField(default='unkown', max_length=50, null=True),
        ),
    ]
