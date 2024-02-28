from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TeacherProfile, Booking, Comment
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, datetime, timedelta


class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('subject', 'date', 'time')  # Adjusted to match model field names

    subject = forms.CharField(label='Subject', max_length=100)
    date = forms.DateField(label='Booking Date', widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(label='Booking Time', widget=forms.TimeInput(attrs={'type': 'time'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise ValidationError('Booking date is required.')
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if not time:
            raise ValidationError('Booking time is required.')
        return time

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            booking_datetime = datetime.combine(date, time)
            if booking_datetime < datetime.now():
                raise ValidationError('Booking must be a future date & time')

        return cleaned_data



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
