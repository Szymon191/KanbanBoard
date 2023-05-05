from django.urls import path
from KanbanBoardApp import views
from KanbanBoardApp.views import tasks, UpdateTask, DeleteTask

app_name = 'KanbanBoardApp'

urlpatterns = [
    path('', tasks, name='toDo'),
    path('add/', views.add, name='add'),
    path('edit/<int:pk>', UpdateTask.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete')
]