from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('booking/<str:teacher_id>/new/', views.create_booking,
         name='create_booking'),
    path('accept_booking/<int:booking_id>/', views.accept_booking,
         name='accept_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking,
         name='delete_booking'),
    path('edit_booking/<int:booking_id>/', views.edit_booking,
         name='edit_booking'),
    path('', views.ReviewList.as_view(), name='Index'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
]
