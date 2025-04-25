from typing import Any

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from photos.services import get_image_tags
from tags.models import Tag


class Photo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    tags = models.ManyToManyField(Tag, related_name="photos", blank=True)

    def add_tags(self) -> None:
        if self.image:
            path = self.image.path
            tags = get_image_tags(path)
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                self.tags.add(tag)


@receiver(post_save, sender=Photo)
def create_tags(sender: type[Photo], instance: Photo, **kwargs: Any) -> None:
    if instance.image:
        instance.add_tags()
