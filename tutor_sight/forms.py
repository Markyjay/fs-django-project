import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TeacherProfile, Booking, Comment
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, timedelta

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['subject', 'booking_date', 'booking_time']
    
    subject = forms.CharField(label='Subject', max_length=100)
    booking_date = forms.DateField(label='Booking Date', widget=forms.DateInput(attrs={'type': 'date'}))
    booking_time = forms.TimeField(label='Booking Time', widget=forms.TimeInput(attrs={'type': 'time'}))

    def clean_booking_datetime(self):
        booking_datetime = self.cleaned_data['booking_datetime']

        # Ensure the selected datetime is not in the past
        if booking_datetime < datetime.now():
            raise ValidationError('Booking date and time cannot be in the past.')

        return booking_datetime

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)