# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-07 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180707_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
