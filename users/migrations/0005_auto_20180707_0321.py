# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-07 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180707_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default=True, null=True, upload_to=users.models.upload_image_path),
        ),
    ]