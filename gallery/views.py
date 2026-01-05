from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Gallery
from .serializers import GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = Gallery.objects.select_related(
            "category",
            "artist"
        ).order_by("-created_at")

        # Filter by category slug
        category_slug = self.request.query_params.get("category")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        # Filter by artist ID
        artist_id = self.request.query_params.get("artist")
        if artist_id:
            queryset = queryset.filter(artist_id=artist_id)

        return queryset
