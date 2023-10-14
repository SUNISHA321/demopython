from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.models import Task
from .forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
#listview
class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'
#Detail view
class Taskdetailview(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'task'
#Updateview
class TaskUpdateview(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')



def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST['task']
        priority=request.POST['priority']
        date=request.POST['date']
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request, "home.html",{'task1':task1})
# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task=Task.objects.get(id=id)
    f=TaskForm(request.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})

