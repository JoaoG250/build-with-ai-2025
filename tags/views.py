from typing import Any

from django.db.models import QuerySet
from django.forms.models import ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import View

from tags.forms import TagForm
from tags.models import Tag


class TagListView(View):
    model = Tag

    def get_query_set(self) -> QuerySet[Tag]:
        return Tag.objects.all()

    def get_context_data(self, form: ModelForm[Tag]) -> dict[str, Any]:
        tags = self.get_query_set().order_by("name")
        return {"form": form, "tag_list": tags}

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = TagForm()
        return render(
            request,
            "tags/tag_list.html",
            self.get_context_data(form),
        )

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseRedirect | HttpResponse:
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag-list")
        return render(
            request,
            "tags/tag_list.html",
            self.get_context_data(form),
        )
