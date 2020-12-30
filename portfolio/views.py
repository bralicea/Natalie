from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import About

def index(request):
    about = About.objects.get()
    return TemplateResponse(request, 'index.html', {"about": about})
