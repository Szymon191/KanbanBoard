from django.urls import path
from KanbanBoardApp import views
from KanbanBoardApp.views import tasks

app_name = 'KanbanBoardApp'

urlpatterns = [
    path('', tasks, name='toDo'),
    path('add/', views.add, name='add'),
    path('<str:task_title>/', views.status, name='status')
]