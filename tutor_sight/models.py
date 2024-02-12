from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class TeacherProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField("profile_image", default='placeholder')
    name = models.CharField(max_length=100)
    bio = models.TextField()
    expertise = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.TextField()
    
class TeacherProfileDetail(models.Model):
    bio = models.TextField()
    expertise = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.TextField()

class Review(models.Model):
    teacher_id = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
