# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 02:44
from __future__ import unicode_literals

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20170802_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='order',
            field=courses.fields.PositionField(default=-1),
        ),
    ]
