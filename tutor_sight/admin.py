from django import forms
from django.contrib import admin
from .models import TeacherProfile, TeacherProfileDetail, Booking
from django_summernote.admin import SummernoteModelAdmin

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['subject', 'day', 'time']

admin.site.register(TeacherProfile)
admin.site.register(TeacherProfileDetail)
