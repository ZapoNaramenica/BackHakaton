# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django.db import models
from django.db.backends.signals import connection_created
from django.db.models.expressions import RawSQL
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible


class LocationManager(models.Manager):

    def nearby(self, latitude, longitude, proximity):
        """
        Return all object which distance to specified coordinates
        is less than proximity given in kilometers
        """
        # Great circle distance formula
        gcd = """
              6371 * acos(
               cos(radians(%s)) * cos(radians(lat))
               * cos(radians(lng) - radians(%s)) +
               sin(radians(%s)) * sin(radians(lat))
              )
              """
        return self.get_queryset()\
                   .annotate(distance=RawSQL(gcd, (latitude,
                                                   longitude,
                                                   latitude)))\
                   .filter(distance__lt=proximity)\
                   .order_by('distance')


@python_2_unicode_compatible
class AccidentData(models.Model):
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    damage = models.CharField(max_length=255)
    desc = models.TextField()
    objects = LocationManager()


    def __str__(self):
        return self.desc[:50]


@receiver(connection_created)
def extend_sqlite(connection=None, **kwargs):
    if connection.vendor == "sqlite":
        # sqlite doesn't natively support math functions, so add them
        cf = connection.connection.create_function
        cf('acos', 1, math.acos)
        cf('cos', 1, math.cos)
        cf('radians', 1, math.radians)
        cf('sin', 1, math.sin)
