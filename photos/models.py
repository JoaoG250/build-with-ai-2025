from django.db import models

from tags.models import Tag


class Photo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    tags = models.ManyToManyField(Tag, related_name="photos", blank=True)
