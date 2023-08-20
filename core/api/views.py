from django.shortcuts import render
from property_management.models import Property, PropertyUnit, PropertyOwner, PropertyManager
from api.serializers import PropertySerializer, PropertyUnitSerializer, PropertyOwnerSerializer, PropertyManagerSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView




class PropertyListView(ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer



class PropertyDetailView(RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    lookup_field = 'pk'



class PropertyUnitListView(ListAPIView):
    queryset = PropertyUnit.objects.all()
    serializer_class = PropertyUnitSerializer

class PropertyOwnerListView(ListAPIView):
    queryset = PropertyOwner.objects.all()
    serializer_class = PropertyOwnerSerializer

class PropertyManagerListView(ListAPIView):
    queryset = PropertyManager.objects.all()
    serializer_class = PropertyManagerSerializer






