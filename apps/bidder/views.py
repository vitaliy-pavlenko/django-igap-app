from rest_framework import viewsets

from bidder.models import Bidder
from bidder.serializer import BidderSerializer


class BidderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bidder.objects.all()
    serializer_class = BidderSerializer
