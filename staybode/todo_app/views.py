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

        todo_data = TodoData.objects.all()
        return render(request, 'home.html', {'todo_list':todo_data})
        
    else:
        data = TodoData.objects.all()
        return render(request, 'home.html', {'todo_list':data})

def todo_task(request,title):
    """ Todo Detailed view """

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
        print "post method"
        print request.POST
        # return HttpResponseRedirect("/todo/home/")
        return HttpResponse("completed")
    else:
        print "else method"
        pass