from django.db import models
from cloudinary.models import CloudinaryField
class Project(models.Model):

    title = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image')
    url = models.URLField(max_length=200)
    github_repository = models.URLField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title  
    