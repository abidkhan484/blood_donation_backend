from django.http.response import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import DonorsSerializer
from .models import Donors

class DonorsAPIView(APIView):
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

        serializer.save()
        response = {
            'email': serializer.data['email'],
            'message': "Donor info saved sucessfully."
        }
        return Response(response, status=status.HTTP_201_CREATED)



class DonorDetailAPIView(APIView):
    def getSingleDonor(self, id):
        try:
            return Donors.objects.get(id=id)
        except Donors.DoesNotExist:
            raise Http404

    def get(self, request, id):
        donor = self.getSingleDonor(id)
        serializer = DonorsSerializer(donor)
        return Response(serializer.data)
    
    def put(self, request, id):
        donor = self.getSingleDonor(id)
        serializer = DonorsSerializer(donor, data=request.data)
        valid = serializer.is_valid(raise_exception=True)
        if not valid:
            raise status.HTTP_400_BAD_REQUEST

        serializer.save()
        response = {
            'email': serializer.data['email'],
            'message': "Donor info updated sucessfully."
        }
        return Response(response)
    
    def delete(self, request, id):
        donor = self.getSingleDonor(id)
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
