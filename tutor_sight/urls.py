from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('booking/<str:teacher_id>/new/', views.create_booking, name='create_booking'),
    path('booking_acceptance/<int:booking_id>/', views.booking_acceptance, name='booking_acceptance'),
    path('booking/<int:booking_id>/delete/', views.delete_booking, name='delete_booking'),
    path('booking/<int:booking_id>/edit/', views.edit_booking, name='edit_booking'),
    path('', views.ReviewList.as_view(), name='Index'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
]