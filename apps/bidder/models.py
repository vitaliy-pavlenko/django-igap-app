from django.db import models


class Bidder(models.Model):
    name = models.CharField(max_length=200)

