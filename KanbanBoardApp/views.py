from django.shortcuts import render, get_object_or_404

from KanbanBoardApp.models import Task


# Create your views here.

def toDo(request):

    toDo = Task.object.all().filter(status="do_zrobienia")
    return render(request, 'tasks/toDo.html', {'todo': toDo})

def inProgress(request):

    inProgress = Task.object.all().filter(status="w_trakcie")
    return render(request, 'tasks/inProgress.html', {'inprogress': inProgress})

def done(request):

    done = Task.object.all().filter(status="zrobione")
    return render(request, 'tasks/toDo.html', {'doNe': done})


