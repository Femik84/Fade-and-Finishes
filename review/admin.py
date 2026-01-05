from django.contrib import admin
from .models import Review
from django.utils.html import format_html

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "stars", "date", "comment", "profile_picture_tag")
    list_filter = ("stars", "date")
    search_fields = ("name", "comment")
    readonly_fields = ("date",)

    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.profile_picture.url)
        return "-"
    profile_picture_tag.short_description = "Profile Picture"
