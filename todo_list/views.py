from django.shortcuts import render
from todo_list.models import Task
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
from datetime import datetime
from todo_list.forms import AddTaskForm


def task(request):
    if request.method == 'GET':
        todo = Task.objects.all()
        result = {
            'todo': todo,
            'add_task_form': AddTaskForm(),
        }
        return render(request, 'main.html', result)

    if request.method == 'POST':
        AddTaskForm(request.POST).save()
        return redirect('/todo/')


def status(request, id_task):
    task_status = Task.objects.get(id=id_task)
    task_status.status = 'Завершено'
    task_status.date_updated = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    task_status.save()
    return redirect('/todo/')


def edit_task(request, id_task):
    edit_todo = Task.objects.get(id=id_task)
    if request.method == 'GET':
        result = {
            'id': edit_todo.id,
            'title': edit_todo.title,
            'text': edit_todo.text,
            'add_task_form': AddTaskForm(instance=edit_todo),
        }
        return render(request, 'edit_task.html', result)

    if request.method == 'POST':
        edit_todo.title = request.POST.get('title')
        edit_todo.text = request.POST.get('text')
        edit_todo.save()
        return redirect('/todo/')


def completed_task(request):
    completed_todo = Task.objects.all()
    result = {
        'completed': completed_todo
    }
    return render(request, 'completed.html', result)


def delete_task(request, id_task):
    Task.objects.get(id=id_task).delete()
    return redirect('/todo/')


