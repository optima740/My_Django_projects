from rest_framework import serializers
from ..models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'date_assembly', 'color', 'of_enterprise')


