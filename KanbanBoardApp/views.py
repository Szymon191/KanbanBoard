from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DeleteView

from KanbanBoardApp.models import Task
from .forms import addForm


def add(request):
    if request.method == 'POST':
        form = addForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = addForm()

    return render(request, 'add/add.html', {'form': form})


def tasks(request):
    toDo = Task.object.all().filter(status="do_zrobienia")
    w_trakcie = Task.object.all().filter(status="w_trakcie")
    done = Task.object.all().filter(status="zrobione")
    return render(request, 'base.html', {'toDo': toDo, 'progres': w_trakcie, 'done': done})


class UpdateTask(UpdateView):
    model = Task
    template_name = 'tasks/update.html'
    fields = ['title', 'body', 'status']

    def get_success_url(self):
        return reverse('KanbanBoardApp:toDo')


class DeleteTask(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'

    def get_success_url(self):
        return reverse('KanbanBoardApp:toDo')