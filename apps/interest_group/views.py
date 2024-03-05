from rest_framework import viewsets

from interest_group.models import InterestGroup
from interest_group.serializer import InterestGroupSerializer


class InterestGroupViewSet(viewsets.ModelViewSet):
    queryset = InterestGroup.objects.all()
    serializer_class = InterestGroupSerializer
