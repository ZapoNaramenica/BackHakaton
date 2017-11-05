from rest_framework import serializers
from accident.models import AccidentData


class AccidentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AccidentData
        fields = ('id', 'lat', 'lng', 'damage', 'desc')

