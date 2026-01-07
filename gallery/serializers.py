from rest_framework import serializers
from .models import Gallery
from categories.models import Category
from categories.serializers import CategorySerializer
from artist.models import Artist
from artist.serializers import ArtistSerializer


class GallerySerializer(serializers.ModelSerializer):
    # READ
    category = CategorySerializer(read_only=True)
    artist = ArtistSerializer(read_only=True)

    # WRITE
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        source="category"
    )

    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        write_only=True,
        source="artist",
        required=False,
        allow_null=True
    )

    class Meta:
        model = Gallery
        fields = [
            "id",
            "name",
            "category",
            "category_id",
            "artist",
            "artist_id",
            "hero_image", 
            "min_price",
            "max_price",
            "is_featured",
            "is_portfolio_grid",
            "created_at",
            "updated_at",
        ]

        read_only_fields = ("created_at", "updated_at")
