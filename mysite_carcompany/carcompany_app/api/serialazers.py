from rest_framework import serializers
from ..models import *

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'color', 'fuel_util', 'date_of_buy', 'of_enterprise')

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('id', 'title', 'address', 'time_zone')

class TripSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('geo_data', 'to_car', 'begin_time', 'save_time', 'end_time')
