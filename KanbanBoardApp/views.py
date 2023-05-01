
from django.http import request
from django.shortcuts import render
from KanbanBoardApp.models import Task
from .forms import TaskForm

# Create your views here.




def tasks(request):
    toDo = Task.object.all().filter(status="do_zrobienia")
    w_trakcie = Task.object.all().filter(status="w_trakcie")
    return render(request, 'base.html', {'toDo': toDo, 'progres': w_trakcie})


def detail(request, task_title):
    once = Task.object.all().filter(title=task_title)
    toDo = Task.object.all().filter(status="do_zrobienia")
    w_trakcie = Task.object.all().filter(status="w_trakcie")

    element = Task.object.all().filter()


    initialDate = {
        'title':task_title,
        'body': element.model.body,
        'status': once.model.status
    }
    #form = TaskForm(initial=initialDate)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            user = form.save()
            # zapisz użytkownika i przekieruj na stronę powodzenia
    else:
        form = TaskForm(initial=initialDate)
    #context = {'form':form}
    return render(request, 'tasks/detail.html', {'toDo': toDo, 'progres': w_trakcie, 'once': once, 'form': form})


def test(request):
    return render(request,'tasks/test.html')





