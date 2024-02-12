from django import forms
from django.contrib import admin
from .models import TeacherProfile, TeacherProfileDetail, Review
from django_summernote.admin import SummernoteModelAdmin

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

admin.site.register(TeacherProfile)
admin.site.register(TeacherProfileDetail)
admin.site.register(Review)
