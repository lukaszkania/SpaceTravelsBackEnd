from rest_framework import serializers
from flights.models import Flight

class FlightSerializer(serializers.HyperlinkedModelSerializer):
    '''Defining what model should be in API and chooseing fields to be displayed'''
    class Meta:
        model = Flight
        fields = ('pk', 'departure_date', 'arrival_date', 'seats_amount', 'ticket_price', 'tourists' )
  