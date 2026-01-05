from rest_framework import serializers
from .models import Review
from service.models import Service  # <- import Service here

class ReviewSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    service = serializers.PrimaryKeyRelatedField(queryset=Service.objects.all())

    class Meta:
        model = Review
        fields = ["id", "service", "name", "date", "stars", "comment", "profile_picture"]
        read_only_fields = ["id", "date"]

    def validate_stars(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Stars must be between 1 and 5.")
        return value
