# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
