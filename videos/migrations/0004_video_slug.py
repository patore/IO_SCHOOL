# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
