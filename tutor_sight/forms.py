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
        fields = ('subject', 'booking_date', 'booking_time')

    subject = forms.CharField(label='Subject', max_length=100)
    booking_date = forms.DateField(label='Booking Date', widget=forms.DateInput
                                   (attrs={'type': 'date'}))
    booking_time = forms.TimeField(label='Booking Time', widget=forms.TimeInput
                                   (attrs={'type': 'time'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_booking_date(self):
        booking_date = self.cleaned_data.get('booking_date')
        if not booking_date:
            raise ValidationError('Booking date is required.')
        return booking_date

    def clean_booking_time(self):
        booking_time = self.cleaned_data.get('booking_time')
        if not booking_time:
            raise ValidationError('Booking time is required.')
        return booking_time

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        if booking_date and booking_time:
            # Combine date and time to create a datetime object
            booking_datetime = datetime.combine(booking_date, booking_time)

            # Ensure the selected datetime is not in the past
            if booking_datetime < datetime.now():
                raise ValidationError('Booking must be a future date & time')

        return cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
