from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.index, name='home'),
    url(r'^(?P<title>[A-Za-z0-9\w @%&._-]+)/', views.todo_task, name='todo_detail'),    
    url(r'^update/', views.todo_update, name='update1'),
    

]

