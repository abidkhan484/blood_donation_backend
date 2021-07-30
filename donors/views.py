from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DonorsSerializer
from .models import Donors

class DonorsView(APIView):
    serializerClass = DonorsSerializer

    def get(self, request):
        queryset = Donors.objects.all()
        serializer = self.serializerClass(queryset, many=True)
        donors = serializer.data
        return Response(donors)

    def post(self, request):
        serializer = self.serializerClass(data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if not valid:
            raise status.HTTP_400_BAD_REQUEST
        elif Donors.objects.filter(email=self.request.data['email']).exists():
            return Response({"error": "This email id already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response = {
            'email': serializer.data['email'],
            'message': "Donor info saved sucessfully."
        }
        return Response(response, status=status.HTTP_201_CREATED)

