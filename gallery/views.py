from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Gallery
from .serializers import GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    parser_classes = (MultiPartParser, FormParser)
    pagination_class = None  

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

        # Filter featured
        is_featured = self.request.query_params.get("featured")
        if is_featured is not None:
            queryset = queryset.filter(is_featured=is_featured.lower() == "true")

        # Filter portfolio grid
        is_portfolio = self.request.query_params.get("portfolio")
        if is_portfolio is not None:
            queryset = queryset.filter(is_portfolio_grid=is_portfolio.lower() == "true")

        return queryset