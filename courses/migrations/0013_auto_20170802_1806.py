# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20170802_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('main', 'Main'), ('sec', 'Secondary')], default='main', max_length=120),
        ),
    ]
