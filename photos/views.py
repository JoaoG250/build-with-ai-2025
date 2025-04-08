from typing import Any

from django.db.models.query import QuerySet
from django.forms.models import ModelForm
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View

from photos.models import Photo


class PhotoListView(ListView[Photo]):
    model = Photo

    def get_queryset(self) -> QuerySet[Photo]:
        queryset = super().get_queryset().order_by("-created_at").prefetch_related("tags")
        tag = self.request.GET.get("tag")
        if tag:
            queryset = queryset.filter(tags__name=tag)
        return queryset


class PhotoCreateView(CreateView[Photo, ModelForm[Photo]]):
    model = Photo
    fields = ["title", "image"]
    success_url = reverse_lazy("photo-list")


class PhotoUpdateView(UpdateView[Photo, ModelForm[Photo]]):
    model = Photo
    fields = ["title", "image", "tags"]
    success_url = reverse_lazy("photo-list")


class PhotoDeleteView(View):
    def post(self, request: HttpRequest, pk: int, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        photo = get_object_or_404(Photo, pk=pk)
        photo.delete()
        return redirect("photo-list")
