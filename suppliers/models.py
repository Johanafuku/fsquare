from django.db import models
from django.contrib.auth.models import User


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fabric_types = models.JSONField(null=True, blank=True)
    colors_available = models.JSONField(null=True, blank=True)
    processing = models.JSONField(null=True, blank=True) #wooven, nonwooven, knitten
    min_meters = models.FloatField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
