from django.db import models
from django.utils.text import slugify
from categories.models import Category


class Service(models.Model):
    ESSENTIAL = "essential"
    PREMIUM = "premium"
    EXCLUSIVE = "exclusive"

    DIFFICULTY_CHOICES = [
        (ESSENTIAL, "Essential – Tier 1"),
        (PREMIUM, "Premium – Tier 2"),
        (EXCLUSIVE, "Exclusive – Tier 3"),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="services"
    )

    difficulty_level = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default=ESSENTIAL
    )

    tagline = models.CharField(max_length=255, blank=True)
    short_description = models.TextField()
    long_description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)

    hero_image = models.ImageField(upload_to="services/hero_images/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Service.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ServiceGallery(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="services/gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gallery image for {self.service.name}"