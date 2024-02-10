from django import forms
from django.contrib import admin
from .models import TeacherProfile, Review, Student
from django_summernote.admin import SummernoteModelAdmin

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

admin.site.register(Review)

admin.site.register(Student)