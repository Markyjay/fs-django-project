from django.shortcuts import render, get_object_or_404, redirect
from .models import TeacherProfile, Review
from .forms import TeacherProfileForm
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView, ListView, View

class Index(ListView):
    model = TeacherProfile
    template_name = 'index.html'
    context_object_name = 'teacherprofiles'

    def get_queryset(self):
        return TeacherProfile.objects.all()

class TeacherProfileDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = TeacherProfile.objects.filter(status=1)
        TeacherProfile = get_object_or_404(queryset, slug=slug)
        
        return render(
                request,
                "profile_detail.html",
                {
                    "teacherprofile": TeacherProfile,
                },
            )

