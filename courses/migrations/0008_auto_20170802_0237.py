# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 02:37
from __future__ import unicode_literals

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20170802_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='order',
            field=courses.fields.PositionField(default=-1),
        ),
    ]