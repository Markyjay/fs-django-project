from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import TeacherProfile, Review, Student
from .forms import TeacherProfileForm
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'index.html')

def teacher_profile_detail(request, teacher_id):
    teacher = get_object_or_404(TeacherProfile, id=teacher_id)
    reviews = Review.objects.filter(teacher_id=teacher_id)

    return render(request, 'teacher_profile_detail.html', {'teacher': teacher, 'reviews': reviews})

def student_profile_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_profile_detail.html', {'student': student})

def create_teacher_profile(request):
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST)
        if form.is_valid():
            teacher_profile = form.save()
            return redirect('teacher_profile_detail', teacher_id=teacher_profile.id)
    else:
        form = TeacherProfileForm()

    return render(request, 'create_teacher_profile.html', {'form': form})