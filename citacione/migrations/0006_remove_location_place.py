# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-14 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('citacione', '0005_image_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='place',
        ),
    ]