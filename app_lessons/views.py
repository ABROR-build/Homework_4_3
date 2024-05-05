from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms


def list_subjects(request):
    subjects = models.Subjects.objects.all()
    context = {
        'subjects': subjects
    }
    return render(request, 'list_subjects.html', context=context)


def list_lessons(request, pk):
    lessons = models.Lessons.objects.filter(subject=pk)
    context = {
        'lessons': lessons
    }
    return render(request, 'list_lessons.html', context=context)


def get_lesson(request, pk):
    lesson = models.Lessons.objects.get(pk=pk)
    context = {
        'lesson': lesson
    }
    return render(request, 'get_lesson.html', context=context)


def add_lesson(request):
    form = forms.LessonForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('list_subjects')
    context = {
        'form': form
    }
    return render(request, 'new.html', context=context)


def edit_lesson(request, pk):
    objects = get_object_or_404(models.Lessons, pk=pk)
    if request.method == 'POST' or 'GET':
        form = forms.LessonForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect('list_subjects')
        else:
            form = forms.LessonForm(instance=objects)

            context = {
                'form': form
            }
            return render(request, 'edit.html', context=context)


def delete_lesson(request, pk):
    objects = get_object_or_404(models.Lessons, pk=pk)
    if request.method == 'POST' or 'GET':
        objects.delete()
        return render(request, 'delete.html')
