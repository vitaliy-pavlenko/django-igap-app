from rest_framework import serializers

from interest_group.models import InterestGroup


class InterestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestGroup
        fields = ['id', 'name', 'bidder', 'description', 'data_fee', 'advertiser', 'availability']
