from django.shortcuts import render, get_object_or_404

from KanbanBoardApp.models import Task


# Create your views here.

def tasks(request):
    toDo = Task.object.all().filter(status="do_zrobienia")
    w_trakcie = Task.object.all().filter(status="w_trakcie")
    done = Task.object.all().filter(status="zrobione")
    return render(request, 'base.html', {'toDo': toDo, 'progress': w_trakcie, 'done': done})




