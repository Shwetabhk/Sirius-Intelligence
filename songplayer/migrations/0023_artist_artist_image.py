# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-31 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songplayer', '0022_auto_20180730_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_image',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]