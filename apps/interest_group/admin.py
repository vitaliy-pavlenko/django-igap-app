from django.contrib import admin

from interest_group.models import InterestGroup


@admin.register(InterestGroup)
class InterestGroupAdmin(admin.ModelAdmin):
    pass
