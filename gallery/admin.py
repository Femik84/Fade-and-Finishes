from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "artist",
        "price_range",
        "created_at",
    )

    list_filter = ("category", "artist")
    search_fields = ("name",)

    readonly_fields = (
        "created_at",
        "updated_at",
        "hero_preview",
        "before_preview",
        "after_preview",
    )

    fieldsets = (
        (None, {
            "fields": ("name", "category", "artist")
        }),
        ("Images", {
            "fields": (
                "hero_image",
                "hero_preview",
                "before_image",
                "before_preview",
                "after_image",
                "after_preview",
            )
        }),
        ("Pricing", {
            "fields": ("min_price", "max_price")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )

    def hero_preview(self, obj):
        if obj.hero_image:
            return format_html(
                '<img src="{}" style="height: 120px;" />',
                obj.hero_image.url
            )
        return "-"

    def before_preview(self, obj):
        if obj.before_image:
            return format_html(
                '<img src="{}" style="height: 120px;" />',
                obj.before_image.url
            )
        return "-"

    def after_preview(self, obj):
        if obj.after_image:
            return format_html(
                '<img src="{}" style="height: 120px;" />',
                obj.after_image.url
            )
        return "-"

    hero_preview.short_description = "Hero Image Preview"
    before_preview.short_description = "Before Image Preview"
    after_preview.short_description = "After Image Preview"

    def price_range(self, obj):
        return f"{obj.min_price} - {obj.max_price}"

    price_range.short_description = "Price Range"
