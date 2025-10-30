from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import HttpResponse

def task_list(request): # hàm task_list lấy tất cả danh sách
    tasks = Task.objects.all().order_by('-created_at')
    incomplete_count = tasks.filter(is_completed=False).count()
    return render(request, 'todo_app/index.html', {'tasks': tasks, 'incomplete_count': incomplete_count})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.is_completed = 'is_completed' in request.POST
        task.save()
    return redirect('task_list')

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('task_list')

def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            task.title = title
        if description is not None:
            task.description = description

        task.save()
        return redirect('task_list')

    # Nếu chỉ GET (hiển thị form sửa)
    return render(request, 'todo_app/edit.html', {'task': task})

def task_delete(request, task_id):
    """Xóa công việc theo ID"""
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo_app/delete.html', {'task': task})
