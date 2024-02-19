from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class TeacherProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=100, primary_key=True)
    profile_image = CloudinaryField("profile_image", default='placeholder')
    name = models.CharField(max_length=100)
    bio = models.TextField()
    expertise = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.TextField()
    
class TeacherProfileDetail(models.Model):
    profile_image = CloudinaryField("profile_image", default='placeholder')
    expertise = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.TextField()

class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(
        max_length=50, null=True, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, default="9 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user} | day: {self.day} | time: {self.time}"

