from django.shortcuts import render
from todo_list.models import Task
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect
from datetime import datetime
from todo_list.forms import AddTaskForm


def task(request):
    todo = Task.objects.all()
    result = {
        'todo': todo,
        'add_task_form': AddTaskForm(),
    }
    if request.method == 'GET':
        return render(request, 'main.html', result)

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo/')

        form.add_error(None, 'Ошибка в создании задачи')
        result['add_task_form'] = form
        return render(request, 'main.html', result)


def status(request, id_task):
    task_status = Task.objects.get(id=id_task)
    task_status.status = 'Завершено'
    task_status.date_updated = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    task_status.save()
    return redirect('/todo/')


def edit_task(request, id_task):
    edit_todo = Task.objects.get(id=id_task)
    result = {
        'id': edit_todo.id,
        'add_task_form': AddTaskForm(instance=edit_todo),
    }

    if request.method == 'GET':
        return render(request, 'edit_task.html', result)

    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            edit_todo.title = request.POST.get('title')
            edit_todo.text = request.POST.get('text')
            edit_todo.save()
            return redirect('/todo/')

        form.add_error(None, 'Ошибка в создании задачи')
        result['add_task_form'] = form
        return render(request, 'edit_task.html', result)


def completed_task(request):
    completed_todo = Task.objects.all()
    result = {
        'completed': completed_todo
    }
    return render(request, 'completed.html', result)


def delete_task(request, id_task):
    Task.objects.get(id=id_task).delete()
    return redirect('/todo/')


