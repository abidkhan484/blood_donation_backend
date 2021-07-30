from .models import Donors
from rest_framework import serializers

class DonorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donors
        fields = ('name', 'bloodGroup', 'phone', 'email', 'lastDonationDate')

