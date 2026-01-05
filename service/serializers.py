from rest_framework import serializers
from .models import Service, ServiceGallery
from review.serializers import ReviewSerializer
from categories.serializers import CategorySerializer  # import Category serializer
from categories.models import Category


class ServiceGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceGallery
        fields = ["id", "image"]


class ServiceSerializer(serializers.ModelSerializer):
    gallery = ServiceGallerySerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, read_only=True)

    # READ: return full category object
    category = CategorySerializer(read_only=True)

    # WRITE: accept category ID
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
            "category",       # nested category (read)
            "category_id",    # category ID (write)
            "gallery",
            "reviews",
        ]
        read_only_fields = ["slug"]

    def create(self, validated_data):
        gallery_data = validated_data.pop("gallery", [])
        service = Service.objects.create(**validated_data)

        if len(gallery_data) > 6:
            raise serializers.ValidationError("Maximum of 6 gallery images allowed.")

        for img in gallery_data:
            ServiceGallery.objects.create(service=service, **img)

        return service

    def update(self, instance, validated_data):
        gallery_data = validated_data.pop("gallery", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if gallery_data is not None:
            instance.gallery.all().delete()

            if len(gallery_data) > 6:
                raise serializers.ValidationError("Maximum of 6 gallery images allowed.")

            for img in gallery_data:
                ServiceGallery.objects.create(service=instance, **img)

        return instance
