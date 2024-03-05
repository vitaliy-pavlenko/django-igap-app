from rest_framework import serializers

from advertiser.models import Advertiser


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = ['id', 'name', 'external_id']
