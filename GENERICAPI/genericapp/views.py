from django.shortcuts import render
from .models import Address, Info
from .serializers import AddressSerializers, InfoSerializers
from rest_framework import generics
# Create your views here.


class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers

class AddressDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializers


class InfoList(generics.ListCreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers


class InfoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers