# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20170806_2337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='categories',
            new_name='category',
        ),
    ]