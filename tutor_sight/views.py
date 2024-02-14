from django.shortcuts import render, get_object_or_404, redirect
from .models import TeacherProfile, Review
from .forms import TeacherProfileForm
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, ListView

class Index(ListView):
    model = TeacherProfile
    template_name = 'index.html'
