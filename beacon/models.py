from uuid import uuid4
from django.db import models


class Beacon(models.Model):
    vehicle_name = models.CharField(max_length=255)
    unique_id = models.CharField(max_length=255, default=uuid4)
    trace = models.CharField(max_length=255)
    instructions = models.TextField()

    def __str__(self):
        return self.unique_id


