from django.db import models


class Typer(models.Model):
    words = models.TextField()
    
    class Meta:
        verbose_name_plural = "Typer"

    def __str__(self):
        return self.words
        
        
class About(models.Model):
    about = models.TextField()
    
    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.about
        

class ImageCategory(models.Model):
    category = models.TextField()
    
    class Meta:
        verbose_name_plural = "Image Category"
    
    def __str__(self):
        return self.category
        
            
class PortfolioImage(models.Model):
    title = models.TextField()
    category = models.TextField()
    image = models.ImageField(upload_to='portfolioimages/')
    
    class Meta:
        verbose_name_plural = "Portfolio Image"
    
    def __str__(self):
        return self.title
        
        
class SketchbookImage(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='sketchbookimages/')
    
    class Meta:
        verbose_name_plural = "Sketchbook Image"
    
    def __str__(self):
        return self.title
