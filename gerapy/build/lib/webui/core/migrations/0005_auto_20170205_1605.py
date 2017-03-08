# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_project_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='code',
            new_name='items',
        ),
        migrations.AddField(
            model_name='project',
            name='pipelines',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='spiders',
            field=models.TextField(blank=True, default=''),
        ),
    ]