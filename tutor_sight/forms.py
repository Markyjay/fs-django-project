import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TeacherProfile, Booking, Comment
from django.core.exceptions import ValidationError
from django.utils import timezone
from tempus_dominus.widgets import DatePicker

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        fields = '__all__'

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ['subject', 'day', 'time']
    
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # Add Bootstrap Datepicker to the 'day' field
        self.fields['day'].widget = DatePicker(
            options={
                'format': 'YYYY-MM-DD',
                'minDate': 'moment()',
                # You can customize other options based on your needs
            },
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)