from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.gis.measure import D
from django.contrib.gis.geos import *
from accident.api.serializers import AccidentSerializer
from accident.models import AccidentData


class GetNearMeAccidents(APIView):

    def get(self, request):
        lat = float(request.GET.get('lat', 0))
        lng = float(request.GET.get('lng', 0))
        distance = request.GET.get('distance', 0.1)
        accidents = AccidentData.objects.nearby(lat, lng, distance)
        serializer = AccidentSerializer(accidents, many=True)
        return Response(serializer.data)


class AccidentList(ListAPIView):
    queryset = AccidentData.objects.all().order_by('-id')[:3000]
    serializer_class = AccidentSerializer

    @method_decorator(cache_page(15))
    def dispatch(self, *args, **kwargs):
        return super(AccidentList, self).dispatch(*args, **kwargs)