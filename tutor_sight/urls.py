from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('teacher/<int:teacher_id>/', views.TeacherProfileDetail.as_view, name='teacherprofiledetail'),
    path('booking/<int:teacher_id>', views.create_booking, name='create_booking'),
    path('booking/<int:pk>/delete/', views.delete_booking, name='delete_booking'),
]