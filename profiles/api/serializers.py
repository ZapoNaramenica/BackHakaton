from rest_framework import serializers
from beacon.models import Beacon
from profiles.models import ProfileRoute, ProfileRouteBus


class ProfileRouteBusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProfileRouteBus
        fields = ('id', 'vehicle_name')


class ProfileRouteSerializer(serializers.HyperlinkedModelSerializer):
    buses = ProfileRouteBusSerializer(many=True, source='profileroutebus_set')

    class Meta:
        model = ProfileRoute
        fields = ('id', 'name', 'profile_id', 'buses')

