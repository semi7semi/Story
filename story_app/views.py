from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from story_app.forms import AddStory
from story_app.models import Story


class Index(View):
    def get(self, request):
        stories = Story.objects.all()
        ctx = {
            "stories": stories
        }
        return render(request, "index.html", ctx)


class AddStoryView(View):
    def get(self, request):
        form = AddStory()
        ctx = {
            "form": form
        }
        return render(request, "add_story.html", ctx)
    def post(self, request):
        form = AddStory(request.POST)
        if form.is_valid():
            story = form.cleaned_data["title"]
            form.save()
            return redirect("main")
