# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_goal_is_locked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='user',
        ),
        migrations.DeleteModel(
            name='Goal',
        ),
    ]
