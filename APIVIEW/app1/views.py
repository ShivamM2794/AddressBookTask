from django.shortcuts import render
from .models import Info, Address
from .serializers import InfoSerializers, AddressSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

@api_view(['GET', 'POST'])
def info_list(request):
    if request.method=='GET':
        info = Info.objects.all()
        serializer = InfoSerializers(info, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = InfoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def info_details(request, pk):
    if request.method == 'GET':
        try:
            info = Info.objects.get(pk=pk)
        except Info.DoesNotExist:
            return Response({'Error':'No Address Found'}, status = status.HTTP_404_NOT_FOUND)
        serializer = InfoSerializers(info)
        return Response(serializer.data)

    if request.method == 'PUT':
        info = Info.objects.get(pk=pk)
        serializer = InfoSerializers(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        info = Info.objects.get(pk=pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddressListView(APIView):

    def get(self, request):
        address = Address.objects.all()
        serializer = AddressSerializers(address, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddressSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AddressDetailsView(APIView):
    def get(self,request,pk):
        try:
            address=Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            return Response({'error':'Address does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AddressSerializers(address)
        return Response(serializer.data)

    def put(self,request,pk):
        address=Address.objects.get(pk=pk)
        serializer = AddressSerializers(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        address=Address.objects.get(pk=pk)
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from faker import Faker
fake = Faker()
import random
from getindianname import *
class Fakedata(APIView):

    def get(self, request):
        for i in range(10):
            f=fake.first_name()
            l=fake.last_name()
            n=random.randint(7020000000,9822999999)
            c=fake.city()
            i=Info(fname=f, lname=l,phoneno=n,city=c)
            i.save()
        return Response(status=status.HTTP_201_CREATED)
        # serializer = InfoSerializers(fname='Abhi', lname='Jeet', phoneno=9876544210, city='PPUUNNEE')
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors)
