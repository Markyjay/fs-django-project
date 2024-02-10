from django.contrib import admin
from . import views
from django.urls import path
from .views import index, teacher_profile_detail, student_profile_detail, create_teacher_profile

app_name = 'tutor_sight'

urlpatterns = [
    path('', index, name='index'),
    path('teacher/<int:teacher_id>/', teacher_profile_detail, name='teacher_profile_detail'),
    path('student/<int:student_id>/', student_profile_detail, name='student_profile_detail'),
    path('create_teacher_profile/', create_teacher_profile, name='create_teacher_profile'),
]