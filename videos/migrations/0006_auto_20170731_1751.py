# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20170731_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]