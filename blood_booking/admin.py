from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    fields = ('name', 'requestedBG', 'contact')

admin.site.register(Booking, BookingAdmin)
