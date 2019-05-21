# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TodoData(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.CharField(max_length=250,blank=True)
    todo_task = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=250,blank=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)