from rest_framework.routers import DefaultRouter
from .views import FlightViewSet

router = DefaultRouter()
router.register('flights', FlightViewSet ,base_name='flight')
urlpatterns = router.urls
