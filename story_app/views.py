from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from datetime import datetime, timedelta, date
from story_app.forms import AddStory, AddPeriodForm
from story_app.models import Story
import calendar
from calendar import HTMLCalendar
from datetime import datetime


class Index(View):
    def get(self, request):
        stories = Story.objects.filter(type="erotic").order_by("-publication_date")
        fantasy = Story.objects.filter(type="fantasy").order_by("-publication_date")
        no_of_stories = Story.objects.count()
        new_time = date.today() - timedelta(days=3)
        print(new_time)
        ctx = {
            "stories": stories,
            "fantasy": fantasy,
            "no_of_stories": no_of_stories,
            "new_time": new_time
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


class CalendarView(View):
    def get(self, request):
        form = AddPeriodForm(initial={"period_length": 30, "period_day": datetime.now()})
        ctx = {
            "form": form,
        }
        return render(request, "calendar.html", ctx)

    def post(self, request):
        form = AddPeriodForm(request.POST)
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        month = now.strftime('%B')
        cal = calendar.Calendar(calendar.MONDAY)
        month_days = cal.monthdatescalendar(current_year, current_month)
        if form.is_valid():
            period_day = form.cleaned_data["period_day"]
            period_length = form.cleaned_data["period_length"]


            ctx = {
                "form": form,
                "month_days": month_days,
                "current_month": current_month,
                "month": month,
                "period_day": period_day,
            }

            return render(request, "calendar.html", ctx)





class StoryDeleteView(View):
    def get(self, request, id):
        story = Story.objects.get(pk=id)
        story.delete()
        return redirect("main")


class TypographyView(View):
    def get(self, request):
        return render(request, "ui-typography.html")