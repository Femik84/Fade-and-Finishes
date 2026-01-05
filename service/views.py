from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    CRUD for Services
    - Lookup by slug
    - Supports file uploads (hero_image + gallery images)
    - Assign category via `category_id` field
    """
    queryset = Service.objects.all().order_by("-created_at")
    serializer_class = ServiceSerializer
    lookup_field = "slug"

    parser_classes = (MultiPartParser, FormParser)
