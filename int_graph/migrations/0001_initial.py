# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QueriesStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(help_text='Query string')),
                ('group', models.IntegerField(blank=True, help_text='group identifier', null=True)),
            ],
        ),
    ]
