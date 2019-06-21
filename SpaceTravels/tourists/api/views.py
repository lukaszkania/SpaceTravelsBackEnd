from rest_framework import viewsets
from tourists.models import Tourist
from .serializers import TouristSerializer

class TouristViewSet(viewsets.ModelViewSet):
    '''A viewsets for viewing and editing Tourist instances'''
    serializer_class = TouristSerializer
    queryset = Tourist.objects.all()