from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Typer, About, PortfolioImage, ImageCategory, SketchbookImage

def index(request):
    typer = Typer.objects.get()
    about = About.objects.get()
    imagecategories = ImageCategory.objects.all()
    portfolioimages = PortfolioImage.objects.all()
    sketchbookimages = SketchbookImage.objects.all()
    return TemplateResponse(request, 'index.html', {"about": about, "portfolioimages": portfolioimages, "imagecategories": imagecategories, "sketchbookimages": sketchbookimages, "typer": typer})
