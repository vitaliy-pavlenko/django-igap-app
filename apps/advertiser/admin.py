from django.contrib import admin

from advertiser.models import Advertiser


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    pass
