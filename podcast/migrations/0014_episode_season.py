# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0013_episode_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='season',
            field=models.PositiveIntegerField(blank=True, help_text='If a serialized show, number of the season', null=True, verbose_name='season'),
        ),
    ]
