from rest_framework import serializers
from .models import Service, ServiceGallery
from categories.serializers import CategorySerializer
from categories.models import Category
from review.models import Review


# --- Service Gallery Serializer ---
class ServiceGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceGallery
        fields = ["id", "image"]


# --- Review (READ-ONLY, LIGHT VERSION) ---
class ServiceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "name",
            "stars",
            "comment",
            "date",
            "profile_picture",
        ]


# --- Service Serializer ---
class ServiceSerializer(serializers.ModelSerializer):
    # READ
    category = CategorySerializer(read_only=True)
    gallery = ServiceGallerySerializer(many=True, read_only=True)
    reviews = ServiceReviewSerializer(many=True, read_only=True)

    # WRITE
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )

    hero_image = serializers.ImageField(required=True)

    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "slug",
            "difficulty_level",
            "tagline",
            "short_description",
            "long_description",
            "price",
            "duration",
            "hero_image",
            "category",        # nested (read)
            "category_id",     # id (write)
            "gallery",
            "reviews",         # ✅ all related reviews
        ]
        read_only_fields = ["slug"]

    def create(self, validated_data):
        service = Service.objects.create(**validated_data)
        return service

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
