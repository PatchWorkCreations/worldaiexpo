from django.contrib import admin
from .models import EventPage, Session, Speaker

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1

@admin.register(EventPage)
class EventPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'venue')
    search_fields = ('title', 'banner_heading', 'venue')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [SessionInline]

    fieldsets = (
        ("Main Details", {
            "fields": ("title", "slug", "banner_heading", "description")
        }),
        ("Event Schedule", {
            "fields": ("event_date", "start_time", "end_time", "venue"),
            "classes": ("collapse",),
        }),
        ("Media", {
            "fields": ("image",),
            "classes": ("collapse",),
        }),
    )

from django.utils.html import format_html

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "thumbnail")
    readonly_fields = ("thumbnail",)
    prepopulated_fields = {"slug": ("name",)}

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.image.url)
        return "No Image"

    thumbnail.short_description = "Preview"

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


#for modal
from .models import GeneralRegistration

admin.site.register(GeneralRegistration)

# myApp/admin.py
from django.contrib import admin
from .models import InternshipApplication

admin.site.register(InternshipApplication)
