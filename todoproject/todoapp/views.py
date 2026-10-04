from django.shortcuts import render,redirect
from .models import Task

def todo(request):

    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)

    tasks = Task.objects.all()

    return render(request, 'todo.html', {'tasks': tasks})


def complete_task(request, id):
    task = Task.objects.get(id=id)
    task.completed = True
    task.save()

    return redirect('todo')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect('todo')

def edit_task(request, id):
    task = Task.objects.get(id=id)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.save()

        return redirect('todo')

    return render(request, 'edit.html', {'task': task})
# Create your views here.

