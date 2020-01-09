from django.urls import path
from project.views import *
from django.conf.urls import include

urlpatterns = [
    path('',get_task, name = 'get_task'),
    path('end_task/<int:pk>',end_task, name='end_task')
]