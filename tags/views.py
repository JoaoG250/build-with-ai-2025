from django.shortcuts import redirect, render
from django.views.generic import View

from tags.forms import TagForm
from tags.models import Tag


class TagListView(View):
    model = Tag

    def get_query_set(self):
        return Tag.objects.all()

    def get_context_data(self, form):
        tags = self.get_query_set().order_by("name")
        return {"form": form, "tag_list": tags}

    def get(self, request, *args, **kwargs):
        form = TagForm()
        return render(
            request,
            "tags/tag_list.html",
            self.get_context_data(form),
        )

    def post(self, request, *args, **kwargs):
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tag-list")
        return render(
            request,
            "tags/tag_list.html",
            self.get_context_data(form),
        )
