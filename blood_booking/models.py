from django.db import models
from django.conf import settings

class Booking(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    requestedBG = models.CharField(max_length=5, choices=settings.BLOOD_GROUPS, blank=False, default='')
    contact = models.CharField(max_length=13, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
