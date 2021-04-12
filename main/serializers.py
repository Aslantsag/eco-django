from rest_framework.serializers import ModelSerializer
from .models import *


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'