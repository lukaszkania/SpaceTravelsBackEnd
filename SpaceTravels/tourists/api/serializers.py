from rest_framework import serializers
from tourists.models import Tourist

class TouristSerializer(serializers.HyperlinkedModelSerializer):
    '''Defining what model should be in API and chooseing fields to be displayed'''
    class Meta:
        model = Tourist
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'birth_date', 'sex', 'country', 'flights' )
