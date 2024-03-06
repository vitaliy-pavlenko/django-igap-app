from rest_framework import serializers

from advertiser.serializer import AdvertiserSerializer
from bidder.serializer import BidderSerializer
from interest_group.models import InterestGroup


class InterestGroupSerializer(serializers.ModelSerializer):
    bidder = BidderSerializer(read_only=True)
    advertiser = AdvertiserSerializer(read_only=True)

    class Meta:
        model = InterestGroup
        fields = ['id', 'name', 'bidder', 'description', 'data_fee', 'advertiser', 'availability']
