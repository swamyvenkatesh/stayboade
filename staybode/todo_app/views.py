# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from models import TodoData

# Create your views here.
def index(request):
    """ Home Page View"""
    if request.method == "POST":
        task = request.POST.get('task')        
        data = TodoData.objects.create(title=str(task))
        
        data = TodoData.objects.all()
        return render(request, 'home.html', {'todo_list':data})
        
    else:
        
        data = TodoData.objects.all()
        return render(request, 'home.html', {'todo_list':data})

def todo_task(request,title):
    """ Todo Detailed view """
    print title, "====================="
    data = TodoData.objects.filter(title__contains=str(title))  
    print data
    title = ''
    desc = ''
    for dd in data:
        title = dd.title
        desc = dd.description      
        
    return render(request, 'update.html', {'title':title, 'desc':desc})

def todo_update(request):
    """ Update view """
    
    if request.method == "GET":        
        title1 = request.POST.get('title')
        status1 = request.POST.get('status')
        desc = request.POST.get('desc')
        TodoData.objects.filter(title__contains=str(title)).update(status=status1, description=desc)
        return HttpResponseRedirect("/todo/home/")
        
    else:
        pass


