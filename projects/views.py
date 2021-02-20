# Django
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def show_projects(request):
    return render(request, 'projects/feed.html')
