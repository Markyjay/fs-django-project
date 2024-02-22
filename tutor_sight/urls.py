from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index.as_view(), name='Index'),
    path('booking/<teacher_id>/new/', views.create_booking, name='create_booking'),
    path('booking_acceptance/<teacher_id>/new/', views.booking_acceptance, name='booking_acceptance'),
    path('', views.ReviewList.as_view(), name='Index'),
    path('<slug:slug>/', views.ReviewDetail.as_view(), name='review_detail'),
    path('like/<slug:slug>', views.ReviewLike.as_view(), name='review_like'),
]