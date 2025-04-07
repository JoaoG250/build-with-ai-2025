from django.db import models


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

    def get_color_class(self):
        color_classes = [
            "btn-primary",
            "btn-secondary",
            "btn-success",
            "btn-danger",
            "btn-warning",
            "btn-info",
            "btn-light",
            "btn-dark",
        ]
        return color_classes[self.id % len(color_classes)]
