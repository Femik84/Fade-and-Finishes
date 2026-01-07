from django.db import models
from categories.models import Category
from artist.models import Artist


class Gallery(models.Model):
    name = models.CharField(max_length=150)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="galleries"
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        related_name="galleries",
        null=True,
        blank=True
    )

    hero_image = models.ImageField(
        upload_to="gallery/hero/"
    )

    min_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    max_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_featured = models.BooleanField(default=False)
    is_portfolio_grid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
