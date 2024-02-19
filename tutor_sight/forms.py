from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TeacherProfile, Booking

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ['subject', 'day', 'time']