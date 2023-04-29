from django.urls import path

from KanbanBoardApp import views

app_name = 'KanbanBoardApp'

urlpatterns = [
    path('', views.tasks, name='tasks'),
]