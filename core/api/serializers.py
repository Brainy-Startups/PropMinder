from rest_framework import serializers
from property_management.models import Property, PropertyUnit, PropertyOwner, PropertyManager


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
    


class PropertyUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyUnit
        fields = '__all__'



class PropertyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyOwner
        fields = '__all__'


class PropertyManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyManager
        fields = '__all__'