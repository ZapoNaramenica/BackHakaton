import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    token = models.CharField(max_length=255, default=uuid.uuid4)

    def __str__(self):
        return self.get_full_name()


class ProfileRoute(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProfileRouteBus(models.Model):
    profile_route = models.ForeignKey(ProfileRoute)
    vehicle_name = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle_name
