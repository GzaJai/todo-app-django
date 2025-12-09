from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo

# Create your views here.
def home_view(request):
    context = {}
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
        context = {'todos': todos}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def create_todo_view(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()

    return render(request, 'create-todo.html', {'form': form})

@login_required(login_url='login')
def todo_details(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)

    return render(request, 'todo-details.html', {'todo': todo})

@login_required(login_url='login')
def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo_details", todo_id=todo.pk)
    else:
        form = TodoForm(instance=todo)

    return render(request, 'edit-todo.html', {'todo': todo, 'form': form})

@login_required(login_url='login')
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)

    if request.method == "POST":
        todo.delete()
        return redirect('home')
    
    return render(request, 'delete-todo.html', {'todo': todo})