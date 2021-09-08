from django import forms
from .models import Story

class AddStory(forms.ModelForm):
    class Meta:
        model = Story
        fields = "__all__"
        labels = {
            "title": "Tytuł",
            "type": "Rodzaj",
            "plot": "Treść",
        }