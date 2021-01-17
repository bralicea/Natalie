from django.contrib import admin

from .models import Typer, About, ImageCategory, PortfolioImage, SketchbookImage

admin.site.register(Typer)
admin.site.register(About)
admin.site.register(ImageCategory)
admin.site.register(PortfolioImage)
admin.site.register(SketchbookImage)
