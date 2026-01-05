from rest_framework.routers import DefaultRouter
from .views import GalleryViewSet

router = DefaultRouter()
router.register(r"galleries", GalleryViewSet, basename="gallery")

urlpatterns = router.urls
