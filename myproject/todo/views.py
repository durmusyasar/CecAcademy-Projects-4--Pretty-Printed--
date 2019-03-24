from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm, NewTodoForm
from django.views.decorators.http import require_POST

def index(request):
    todo_list = Todo.objects.order_by('id')
    newtodoform = NewTodoForm
    context = {
        'todo_list' : todo_list,
        'form' : newtodoform
        }
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=form.cleaned_data['text'])
        new_todo.save()
    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')


# @require_POST
# def addTodo(request):
#     todo_6 = Todo.objects.get(pk=8)
#     form = NewTodoForm(request.POST, instance=todo_6)
#     if form.is_valid():
#         new_todo = form.save()
#     return redirect('index')