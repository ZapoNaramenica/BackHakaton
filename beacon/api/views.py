from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from beacon.api.serializers import BeaconSerializer
from beacon.models import Beacon


class BeaconList(ListCreateAPIView):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(BeaconList, self).dispatch(*args, **kwargs)


class BeaconUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer


class RetrieveBeaconView(generics.RetrieveAPIView):
    queryset = Beacon.objects.all()
    serializer_class = BeaconSerializer
    lookup_field = 'unique_id'