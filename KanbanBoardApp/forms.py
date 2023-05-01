from django import forms
from django.forms import ModelForm
from KanbanBoardApp.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','body','status']
