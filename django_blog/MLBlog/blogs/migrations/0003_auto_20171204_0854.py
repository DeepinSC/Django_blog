# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-04 08:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20171204_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL),
        ),
    ]
