from rest_framework.routers import DefaultRouter
from .views import ArtistViewSet, SpecialtyViewSet

router = DefaultRouter()
router.register(r"artists", ArtistViewSet)
router.register(r"specialties", SpecialtyViewSet)

urlpatterns = router.urls
