from rest_framework import serializers
from .models import Review
from service.models import Service


class ReviewSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)

    # WRITE: accept service IDs
    services = serializers.PrimaryKeyRelatedField(
        queryset=Service.objects.all(),
        many=True
    )

    class Meta:
        model = Review
        fields = [
            "id",
            "services",
            "name",
            "date",
            "stars",
            "comment",
            "profile_picture",
        ]
        read_only_fields = ["id", "date"]

    def validate_stars(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Stars must be between 1 and 5.")
        return value

    def create(self, validated_data):
        services = validated_data.pop("services")
        review = Review.objects.create(**validated_data)
        review.services.set(services)
        return review

    def update(self, instance, validated_data):
        services = validated_data.pop("services", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if services is not None:
            instance.services.set(services)

        return instance
