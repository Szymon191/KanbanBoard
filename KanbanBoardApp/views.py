from django.http import request
from django.shortcuts import render, redirect

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

def status(request, task_title):
    once = Task.object.all().filter(title=task_title)
    toDo = Task.object.all().filter(status="do_zrobienia")
    w_trakcie = Task.object.all().filter(status="w_trakcie")
    return render(request, 'tasks/detail.html', {'toDo': toDo, 'progres': w_trakcie, 'once': once})