from rest_framework import viewsets

from advertiser.models import Advertiser
from advertiser.serializer import AdvertiserSerializer


class AdvertiserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer
