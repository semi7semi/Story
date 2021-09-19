from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from datetime import datetime
from story_app.forms import AddStory
from story_app.models import Story


class Index(View):
    def get(self, request):
        stories = Story.objects.all().order_by("-publication_date")
        no_of_stories = Story.objects.count()
        ctx = {
            "stories": stories,
            "no_of_stories": no_of_stories
        }
        return render(request, "index.html", ctx)


class AddStoryView(View):
    def get(self, request):
        form = AddStory(initial={"publication_date": datetime.now()})
        ctx = {
            "form": form
        }
        return render(request, "story_add.html", ctx)
    def post(self, request):
        form = AddStory(request.POST)
        if form.is_valid():
            story = form.cleaned_data["title"]
            code = form.cleaned_data["code"]
            if code == "maxlove":
                form.save()
            return redirect("main")


class StoryDetailsView(View):
    def get(self, request, id):
        story = Story.objects.get(pk=id)
        ctx = {
            "story": story
        }
        return render(request, "story.html", ctx)


class StoryDeleteView(View):
    def get(self, request, id):
        story = Story.objects.get(pk=id)
        story.delete()
        return redirect("main")


class TypographyView(View):
    def get(self, request):
        return render(request, "ui-typography.html")