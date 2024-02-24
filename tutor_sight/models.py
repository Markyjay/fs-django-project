from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class TeacherProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=100, primary_key=True)
    profile_image = CloudinaryField("profile_image", default='placeholder')
    name = models.CharField(max_length=100)
    bio = models.TextField()
    expertise = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    availability = models.TextField()
    
class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    teacher_profile = models.ForeignKey(
        TeacherProfile, on_delete=models.CASCADE, related_name='reviews'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='reviewpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                             related_name="reviews")
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(
        max_length=50, null=True, blank=True)
    day = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, default="9 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length=20, default="pending")

    def __str__(self):
        return f"{self.user} | day: {self.day} | time: {self.time}"

