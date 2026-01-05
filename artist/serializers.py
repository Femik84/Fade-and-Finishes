from rest_framework import serializers
from .models import Artist, Specialty


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = [
            "id",
            "name",
            "description",
        ]
class ArtistSerializer(serializers.ModelSerializer):
    specialties = SpecialtySerializer(many=True, read_only=True)
    specialty_ids = serializers.PrimaryKeyRelatedField(
        queryset=Specialty.objects.all(),
        many=True,
        write_only=True,
        source="specialties"
    )

    class Meta:
        model = Artist
        fields = [
            "id",
            "name",
            "photo",
            "specialties",
            "specialty_ids",
            "created_at",
            "updated_at",
        ]
