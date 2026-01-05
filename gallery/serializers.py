from rest_framework import serializers
from .models import Gallery
from categories.serializers import CategorySerializer
from .models import Artist
from artist.serializers import ArtistSerializer
from artist.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = [
            "id",
            "name",
            "photo",
        ]



class GallerySerializer(serializers.ModelSerializer):
    # READ
    category = CategorySerializer(read_only=True)
    artist = ArtistSerializer(read_only=True)

    # WRITE
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Gallery._meta.get_field("category").remote_field.model.objects.all(),
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
            "before_image",
            "after_image",
            "min_price",
            "max_price",
            "created_at",
            "updated_at",
        ]

        read_only_fields = ("created_at", "updated_at")
