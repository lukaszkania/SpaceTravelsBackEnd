from rest_framework.routers import DefaultRouter
from .views import TouristViewSet

router = DefaultRouter()
router.register('tourists', TouristViewSet ,base_name='tourist')
urlpatterns = router.urls
