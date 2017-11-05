"""naramenica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from accident.api.views import GetNearMeAccidents, AccidentList
from beacon.api.views import BeaconList, BeaconUpdateDestroyView, RetrieveBeaconView
from profiles.api.views import ProfileRouteList, ProfileRouteUpdateDestroyView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/beacons/$', BeaconList.as_view()),
    url(r'^api/v1/beacons/retrieve/(?P<unique_id>[0-9a-f-]+)/$', RetrieveBeaconView.as_view()),
    url(r'^api/v1/beacons/(?P<pk>[0-9]+)/$', BeaconUpdateDestroyView.as_view()),
    url(r'^api/v1/profile-routes/$', ProfileRouteList.as_view()),
    url(r'^api/v1/accidents/near/$', GetNearMeAccidents.as_view()),
    url(r'^api/v1/accidents/$', AccidentList.as_view()),
    url(r'^api/v1/profile-routes/(?P<pk>[0-9]+)/$', ProfileRouteUpdateDestroyView.as_view()),
]
