from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    fields = ('name', 'problem_description', 'requested_blood_group', 'units', 'contact')

admin.site.register(Booking, BookingAdmin)
