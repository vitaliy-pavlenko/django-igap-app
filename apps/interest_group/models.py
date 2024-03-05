from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q

from advertiser.models import Advertiser
from bidder.models import Bidder


class InterestGroup(models.Model):
    name = models.CharField(max_length=200)
    bidder = models.ForeignKey(Bidder, on_delete=models.PROTECT, related_name="interest_groups")
    description = models.TextField(null=True, blank=True)
    data_fee = models.FloatField(
        validators=[
            MinValueValidator(0),
        ],
        blank=True,
        null=True,
    )
    advertiser = models.ForeignKey(Advertiser, on_delete=models.PROTECT, related_name="interest_groups", null=True, blank=True)
    availability = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(availability=True, advertiser__isnull=True) |
                      Q(availability=False, advertiser__isnull=False),
                name='advertiser_availability_validation'
            )
        ]
