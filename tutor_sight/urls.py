from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    # path('teacher/<int:teacher_id>/', views.teacher_profile_detail.as_view, name='teacher_profile_detail'),
    # path('teacher_profile/', views.teacher_profile.as_view, name='teacher_profile'),
]