# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-27 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songplayer', '0017_auto_20180727_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
