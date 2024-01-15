from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ("Welcome to tutorsight-a site that carefully links students in need to a tutor that can help.")