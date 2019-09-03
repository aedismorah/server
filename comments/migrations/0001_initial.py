# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-27 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentor', models.CharField(max_length=32)),
                ('comment', models.CharField(max_length=10000)),
                ('time', models.CharField(max_length=32)),
            ],
        ),
    ]
