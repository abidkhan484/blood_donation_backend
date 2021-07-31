from django.urls import path
from .views import DonorsAPIView, DonorDetailAPIView

urlpatterns = [
    path('donors/', DonorsAPIView.as_view(), name="donorsListing"),
    path('donor/<int:id>/', DonorDetailAPIView.as_view(), name="donorDetails"),
]
