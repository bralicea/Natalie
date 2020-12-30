from django.db import models

class About(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about
