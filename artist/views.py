from rest_framework import viewsets
from .models import Artist, Specialty
from .serializers import ArtistSerializer, SpecialtySerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.prefetch_related("specialties")
    serializer_class = ArtistSerializer
