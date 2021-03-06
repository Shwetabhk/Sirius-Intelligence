# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-30 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songplayer', '0018_auto_20180727_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='artist_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
