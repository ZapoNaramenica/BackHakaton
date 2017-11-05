from django.contrib import admin
from profiles.models import Profile, ProfileRoute, ProfileRouteBus

admin.site.register(Profile)
admin.site.register(ProfileRoute)
admin.site.register(ProfileRouteBus)