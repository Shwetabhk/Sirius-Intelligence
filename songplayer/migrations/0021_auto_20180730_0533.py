# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-30 05:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songplayer', '0020_auto_20180730_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]