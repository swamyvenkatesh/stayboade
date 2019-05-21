# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-19 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('todo_task', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, max_length=250)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]