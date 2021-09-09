from django.shortcuts import render, redirect
from django.http import HttpResponse #HttpResponse import

from .models import *
from .forms import *

# Create your views here.

#Saves form upon refresh
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}

    return render(request, 'tasks/list.html', context)

#updateTask view
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context={'form':form}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'tasks/updateTask.html', context)

#deleteTask view
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request,'tasks/deleteTask.html', context)
 