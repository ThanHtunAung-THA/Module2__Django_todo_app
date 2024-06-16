from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})


def todo_create(request):
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST.get('title', ''),
            description = request.POST.get('description', '')
        )
        if new_todo.title:
            new_todo.save()
            return redirect('todo_list')
        else:
            return render(request, 'todo_form.html', {'error': 'title cannot be empty.'})
        
    return render(request, 'todo_list.html')


def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_confirm_delete.html', {'todo' : todo})


def todo_complete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')


def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title', todo.title)
        todo.description = request.POST.get('description', todo.description)
        if todo.title:
            todo.save()
            return redirect('todo_list')
        else:
            return render(request, 'todo_form.html', {'todo': todo, 'error': 'Title cannot be empty.' })

    return render(request, 'todo_edit.html', {'todo': todo})
        
# crud -> post, get ,ged, delete