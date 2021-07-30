from django.urls import path
from .views import DonorsView

urlpatterns = [
    path('', DonorsView.as_view(), name="donorsListing"),
]
