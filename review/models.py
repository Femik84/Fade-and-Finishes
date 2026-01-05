from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from service.models import Service  

class Review(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    stars = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    profile_picture = models.ImageField(
        upload_to="reviews/profile_pictures/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} - {self.stars}⭐"
