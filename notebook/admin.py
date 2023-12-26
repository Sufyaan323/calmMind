from django.contrib import admin
from .models import *

admin.site.site_header = "CalmMind Administration"

# Register your models here.

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


@admin.register(note)
class noteAdmin(admin.ModelAdmin):
    list_display = ("noteId_vanity", "noteTitle_vanity", "noteAuthor_vanity", "noteCreationDate_vanity", "noteModifiedDate_vanity")
    list_display_links = ("noteId_vanity", "noteTitle_vanity", "noteAuthor_vanity", "noteCreationDate_vanity", "noteModifiedDate_vanity")
    list_filter = [("noteAuthor", custom_titled_filter("Authors"))]
    search_fields = ["noteTitle"]
    ordering = ["noteId"]

    def noteId_vanity(self, obj):
        return obj.noteId
    noteId_vanity.short_description = "ID"

    def noteTitle_vanity(self, obj):
        return obj.noteTitle
    noteTitle_vanity.short_description = "Title"

    def noteAuthor_vanity(self, obj):
        return obj.noteAuthor
    noteAuthor_vanity.short_description = "Author"

    def noteCreationDate_vanity(self, obj):
        return obj.noteCreationDate
    noteCreationDate_vanity.short_description = "Creation Date"

    def noteModifiedDate_vanity(self, obj):
        return obj.noteModifiedDate
    noteModifiedDate_vanity.short_description = "Modified Date"