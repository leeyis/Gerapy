# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_project_middlewares'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.TextField(blank=True, default=''),
        ),
    ]
