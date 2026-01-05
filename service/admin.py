from django.contrib import admin
from django.utils.html import format_html

from .models import Service, ServiceGallery


# --- Service Gallery Inline (FK = OK) ---
class ServiceGalleryInline(admin.TabularInline):
    model = ServiceGallery
    extra = 1
    max_num = 6
    readonly_fields = ("uploaded_at",)


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

    inlines = [ServiceGalleryInline]

    # 👇 shows ONLY on the service detail page
    readonly_fields = ("reviews_preview",)

    # --- Read-only reviews display ---
    def reviews_preview(self, obj):
        reviews = obj.reviews.all()

        if not reviews.exists():
            return "No reviews yet"

        return format_html(
            "<div style='margin-top:10px;'>"
            + "".join(
                f"""
                <div style="margin-bottom:8px; padding-bottom:6px; border-bottom:1px solid #eee;">
                    <strong>{r.name}</strong>
                    <span style="color:#f5a623;">{'★' * r.stars}</span><br/>
                    <small>{r.comment[:100]}{'...' if len(r.comment) > 100 else ''}</small>
                </div>
                """
                for r in reviews
            )
            + "</div>"
        )

    reviews_preview.short_description = "Reviews"
