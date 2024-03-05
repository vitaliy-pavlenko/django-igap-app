from django.contrib import admin

from bidder.models import Bidder


@admin.register(Bidder)
class BidderAdmin(admin.ModelAdmin):
    pass
