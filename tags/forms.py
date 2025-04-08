from django.forms import ModelForm

from tags.models import Tag


class TagForm(ModelForm[Tag]):
    class Meta:
        model = Tag
        fields = ["name"]
