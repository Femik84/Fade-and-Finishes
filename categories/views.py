from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    """
    List all categories or create a new one
    """
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a category by slug
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug"
