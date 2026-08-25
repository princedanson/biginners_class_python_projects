from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import CreateTask
from .models import ToDoList

# Handles creating and listing tasks for the todo page.
# If the request is a POST, it validates the submitted form and saves a new task.
# Otherwise, it loads the form and all existing tasks to display in the template.
def PostTask(request):
    if request.method == "POST":
        form = CreateTask(request.POST)
        # print(form)
        if form.is_valid():
            task = form.cleaned_data['Creattast']
            task = ToDoList(task=task)
            task.save()
            return HttpResponseRedirect("/todolist/")
    else:
        form = CreateTask()
        task = ToDoList.objects.all()
        # print(task.values())
    return render(
        request,
        'index.html',
        {
            'form': form,
            'tasks': task
        }
    )

# Deletes selected tasks from the database.
# It reads the selected task IDs from the GET request and removes them.
def DeleteTask(request):
    if request.method == "GET":
        select_task_id = request.GET.getlist('tasks')
        print("This id the tasks", select_task_id)
        delete = ToDoList.objects.filter(id__in=select_task_id).delete()
    return HttpResponseRedirect("/todolist/")



