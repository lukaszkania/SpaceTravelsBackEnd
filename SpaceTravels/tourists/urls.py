from django.urls import path
from .views import TouristCreateView

app_name="tourists"
urlpatterns = [
    path('', TouristCreateView.as_view(), name='register'),
]
