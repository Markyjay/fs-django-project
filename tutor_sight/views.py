from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import HttpResponse
from django.template import loader

class PostList(generic.Listview):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

# Create your views here.
def index(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render)
    