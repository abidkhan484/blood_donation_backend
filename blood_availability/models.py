from django.db import models
from django.conf import settings

class BloodAvailabitity(models.Model):
    blood_group = models.CharField(max_length=5, choices=settings.BLOOD_GROUPS, blank=False, default='')
    availability = models.IntegerField(blank=False, default=0)
    updated_at = models.DateTimeField(auto_now=True)
