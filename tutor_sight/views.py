from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import HttpResponse
from django.template import loader

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

def index(request):
    return render(request,'index.html')