from django import forms
from .models import Story

class AddStory(forms.ModelForm):
    code = forms.CharField(max_length=8, label="Kod")
    class Meta:
        model = Story
        fields = "__all__"
        labels = {
            "title": "Tytuł",
            "type": "Rodzaj",
            "plot": "Treść",
        }