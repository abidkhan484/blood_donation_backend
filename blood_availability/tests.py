from django.test import TestCase
from .views import BloodAvailabitityInBank

class BloodAvailabitity(TestCase):
    
    def test_check_blood_availablity_return_empty(self):
        bloodAvailableClass = BloodAvailabitityInBank()
        availableBlood = bloodAvailableClass.checkAvailableBlood()
        self.assertIsInstance(availableBlood, dict)
    
    def test_check_blood_availability_return_non_integer(self):
        bloodAvailableClass = BloodAvailabitityInBank()
        availableBlood = bloodAvailableClass.checkAvailableBlood()
