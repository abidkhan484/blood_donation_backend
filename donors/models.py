from django.db import models
from django.conf import settings

# Create your models here.
class Donors(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    bloodGroup = models.CharField(max_length=5, choices=settings.BLOOD_GROUPS, blank=False, default='')
    email = models.EmailField(max_length=254, unique=True, blank=False, default='')
    phone = models.CharField(max_length=20, blank=False, default='')
    lastDonationDate = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
