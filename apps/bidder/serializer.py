from rest_framework import serializers

from bidder.models import Bidder


class BidderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bidder
        fields = ['id', 'name']
