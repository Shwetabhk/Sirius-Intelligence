# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-11 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=40)),
            ],
        ),
    ]
