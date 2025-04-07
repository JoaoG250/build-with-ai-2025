from django.forms import ModelForm

from tags.models import Tag


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
