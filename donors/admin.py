from django.contrib import admin
from .models import Donors

class DonorsAdmin(admin.ModelAdmin):
    fields = ('name', 'bloodGroup', 'phone', 'email', 'lastDonationDate')

admin.site.register(Donors, DonorsAdmin)
