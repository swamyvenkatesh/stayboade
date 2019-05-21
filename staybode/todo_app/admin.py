# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TodoData
import csv
from django.http import HttpResponse
from django.utils.translation import gettext as _
# Register your models here.


class Tododetails(admin.ModelAdmin):
    actions = ['download_csv']
    list_display = ('title', 'description','todo_task','status','created_at','modified_at')
    search_fields = ['title']
    list_filter = ('title', )
    def download_csv(self, request, queryset):
        f = open('some.csv', 'wb')
        writer = csv.writer(f)
        writer.writerow(['title', 'description','todo_task','status','created_at','modified_at'])

        for s in queryset:
            writer.writerow([s.title, s.description, s.todo_task, s.status, s.created_at, s.modified_at])

        f.close()

        f = open('some.csv', 'r')
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

admin.site.register(TodoData,Tododetails)

