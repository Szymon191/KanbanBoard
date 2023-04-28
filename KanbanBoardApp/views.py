from django.shortcuts import render

from KanbanBoardApp.models import Task


# Create your views here.


def toDo(request):

    toDo = Task.object.all().filter(status="do_zrobienia")
    return render(request, 'index/toDo.html', {'todo': toDo})
