# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Models
from projects.models import Project
# Create your views here.


def show_projects(request):
    project = Project.objects.all()

    return render(request, 'projects/feed.html', {'projects' : project})
