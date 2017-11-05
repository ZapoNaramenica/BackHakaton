from rest_framework import serializers
from beacon.models import Beacon


class BeaconSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beacon
        fields = ('id', 'vehicle_name', 'unique_id', 'trace', 'instructions')

