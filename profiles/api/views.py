from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from profiles.api.serializers import ProfileRouteSerializer
from profiles.models import ProfileRoute


class ProfileRouteList(ListCreateAPIView):
    queryset = ProfileRoute.objects.all()
    serializer_class = ProfileRouteSerializer


class ProfileRouteUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ProfileRoute.objects.all()
    serializer_class = ProfileRouteSerializer

