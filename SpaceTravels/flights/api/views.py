from rest_framework import viewsets
from flights.models import Flight
from .serializers import FlightSerializer

class FlightViewSet(viewsets.ModelViewSet):
    '''A viewsets for viewing and editing Tourist instances'''
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()