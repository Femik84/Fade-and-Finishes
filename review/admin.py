from django.contrib import admin
from django.utils.html import format_html
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "stars",
        "date",
        "get_services",
        "profile_picture_tag",
    )

    list_filter = ("stars", "date")
    search_fields = ("name", "comment")

    readonly_fields = ("date", "profile_picture_tag")

    filter_horizontal = ("services",)  # ✅ allows multiple service selection

    def get_services(self, obj):
        return ", ".join([service.name for service in obj.services.all()])

    get_services.short_description = "Services"

    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 50%;" />',
                obj.profile_picture.url
            )
        return "-"

    profile_picture_tag.short_description = "Profile Picture"
