from django.contrib import admin
from django.utils.html import format_html

from .models import Service, ServiceGallery
from review.models import Review


# --- Service Gallery Inline ---
class ServiceGalleryInline(admin.TabularInline):
    model = ServiceGallery
    extra = 1
    max_num = 6
    readonly_fields = ("uploaded_at",)


# --- Review Inline ---
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("date", "profile_picture_tag")
    fields = ("name", "stars", "comment", "profile_picture", "profile_picture_tag")

    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 50%;" />',
                obj.profile_picture.url
            )
        return "-"

    profile_picture_tag.short_description = "Profile Picture"


# --- Service Admin ---
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "difficulty_level",
        "price",
        "duration",
        "created_at",
    )

    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "tagline", "short_description")
    list_filter = ("category", "difficulty_level")

    inlines = [ServiceGalleryInline, ReviewInline]
