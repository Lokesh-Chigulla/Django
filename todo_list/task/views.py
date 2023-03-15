from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def main(request):
    tasks= Task.objects.all()
    if request.method=='POST':
        title=request.POST.get('title')
        #complete=request.POST.get('complete')
        user=Task.objects.create(title=title)
        user.save()
    context={'tasks':tasks}
    return render(request, 'main.html', context)

def update_task(request, pk):
    task= get_object_or_404(Task,id=pk)
    if request.method=='POST':
        title=request.POST.get('title')
        task.title= title
        task.save()
        return redirect('home')
    return render( request, 'update_task.html',{'task': task})

def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context= {'item': item}
    return render(request, 'delete.html',  context)