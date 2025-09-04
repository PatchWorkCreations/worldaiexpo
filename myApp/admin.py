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

# myApp/admin.py
from django.contrib import admin
from .models import SponsorInquiry, InternshipApplication  # add any others you register

@admin.register(SponsorInquiry)
class SponsorInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'tier', 'email', 'whatsapp', 'created_at')
    list_filter = ('tier', 'created_at')
    search_fields = ('name', 'company', 'email', 'whatsapp')

from django.contrib import admin
from .models import ExhibitRegistration2  # import both

@admin.register(ExhibitRegistration2)
class ExhibitRegistration2Admin(admin.ModelAdmin):
    list_display = (
        "company_name", "contact_name", "email",
        "tier", "pricing_mode",
        "base_price_peso", "total_price_peso",
        "created_at",
    )
    list_display_links = ("company_name", "contact_name")
    list_filter = ("tier", "pricing_mode", "company_size", "created_at")
    search_fields = ("company_name", "contact_name", "email", "phone", "industry", "website")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Company", {"fields": ("company_name", "company_size", "industry", "website")}),
        ("Primary Contact", {"fields": ("contact_name", "email", "phone")}),
        ("Package", {"fields": ("tier", "pricing_mode")}),
        ("Pricing (PHP)", {"fields": ("base_price", "total_price")}),
        ("Add-ons", {"fields": ("add_logo", "add_power", "add_leads")}),
        ("Other", {"fields": ("notes", "agree")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
