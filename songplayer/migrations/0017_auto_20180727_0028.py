# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-27 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songplayer', '0016_artist_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='image',
        ),
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
