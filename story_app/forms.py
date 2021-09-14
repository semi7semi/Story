from django import forms
from .models import Story

class AddStory(forms.ModelForm):
    code = forms.CharField(max_length=8, label="Kod", widget=forms.TextInput(attrs={'class': "form-control"}))
    class Meta:
        model = Story
        fields = "__all__"
        labels = {
            "title": "Tytuł",
            "type": "Rodzaj",
            "plot": "Treść",
        }
        widgets = {
            "title": forms.TextInput(attrs={'class': "form-control"}),
            "type": forms.Select(attrs={'class': "form-control"}),
            "plot": forms.Textarea(attrs={'class': "form-control", 'cols': 100, 'rows': 100}),
        }