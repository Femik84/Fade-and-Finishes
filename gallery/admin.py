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
        "is_featured",
        "is_portfolio_grid",
        "created_at",
    )

    list_filter = (
        "category",
        "artist",
        "is_featured",
        "is_portfolio_grid",
    )

    search_fields = ("name",)

    readonly_fields = (
        "created_at",
        "updated_at",
        "hero_preview",
    )

    fieldsets = (
        (None, {
            "fields": ("name", "category", "artist")
        }),
        ("Images", {
            "fields": ("hero_image", "hero_preview")
        }),
        ("Pricing", {
            "fields": ("min_price", "max_price")
        }),
        ("Display Options", {
            "fields": ("is_featured", "is_portfolio_grid")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at")
        }),
    )

    def hero_preview(self, obj):
        if obj.hero_image:
            return format_html(
                '<img src="{}" style="height: 120px; border-radius: 6px;" />',
                obj.hero_image.url
            )
        return "-"

    hero_preview.short_description = "Hero Image Preview"

    def price_range(self, obj):
        return f"{obj.min_price} - {obj.max_price}"

    price_range.short_description = "Price Range"
