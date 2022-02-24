from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import TodoItem

# Create your views here.
def index(request):
    completed_todos = TodoItem.objects.filter(completed=True)
    todos = TodoItem.objects.filter(completed=False)
    return render(request, 'index.html', {
        'completed_todos': completed_todos,
        'todos': todos,
    })

def addTodo(request):
    new_todo = TodoItem(task_name=request.POST['task_name'])
    new_todo.save()
    return HttpResponseRedirect('/')

class DeleteTodo(View):
    def get(self, request, todo_id):
        current_todo = TodoItem.objects.get(id=todo_id)
        return render(request, 'delete.html', {
            'current_todo': current_todo,
        })

    def post(self, request, todo_id):
        current_todo = TodoItem.objects.get(id=todo_id)
        current_todo.delete()
        return HttpResponseRedirect('/')


def completeTodo(request, todo_id):
    current_todo = TodoItem.objects.get(id=todo_id)
    current_todo.completed = True
    current_todo.save()
    return HttpResponseRedirect('/')

class UpdateTodo(View):
    def get(self, request, todo_id):
        current_todo = TodoItem.objects.get(id=todo_id)
        return render(request, 'update.html', {
            'current_todo': current_todo,
        })

    def post(self, request, todo_id):
        current_todo = TodoItem.objects.get(id=todo_id)
        current_todo.task_name = request.POST['task_name']
        if 'completed' in request.POST:
            current_todo.completed = True

        else:
            current_todo.completed = False
        current_todo.save()
        return HttpResponseRedirect('/')