from django.contrib import admin

# Register your models here.
from story_app.models import Story


class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "plot", "publication_date")
    list_editable = ("type", "plot")

admin.site.register(Story, StoryAdmin)