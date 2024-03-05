from django.db import models


class Advertiser(models.Model):
    name = models.CharField(max_length=200)
    external_id = models.CharField(max_length=30)
