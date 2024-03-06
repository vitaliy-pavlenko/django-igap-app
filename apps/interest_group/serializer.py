from rest_framework import serializers

from interest_group.models import InterestGroup


class InterestGroupSerializer(serializers.ModelSerializer):
    bidder_name = serializers.CharField(source='bidder.name', read_only=True)
    advertiser_name = serializers.CharField(source='advertiser.name', read_only=True)

    class Meta:
        model = InterestGroup
        fields = (
            'id',
            'name',
            'bidder',
            'bidder_name',
            'description',
            'data_fee',
            'advertiser',
            'advertiser_name',
            'availability'
        )
