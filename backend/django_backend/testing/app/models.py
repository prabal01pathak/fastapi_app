from django.db import models

class ExtraDetails(models.Model):
    city = models.CharField(max_length=100, blank=True)
    pin_code = models.CharField(max_length=10, blank=True)

