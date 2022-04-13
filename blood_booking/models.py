from django.db import models
from django.conf import settings

class Booking(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    problem_description = models.CharField(max_length=255, default='')
    requested_blood_group = models.CharField(max_length=5, choices=settings.BLOOD_GROUPS, blank=False, default='')
    units = models.IntegerField(blank=False, default=0)
    contact = models.CharField(max_length=13, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
