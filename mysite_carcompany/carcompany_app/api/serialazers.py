from rest_framework import serializers
from ..models import Car, Enterprise

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'brand', 'model', 'color', 'fuel_util', 'date_assembly', 'of_enterprise')

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('id', 'title', 'address')

        """
        id = serializers.CharField()
        title = serializers.CharField()
        address = serializers.CharField()

    
    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # переопределяем метод для обновления полей модели Car.
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.fuel_util = validated_data.get('fuel_util', instance.fuel_util)
        instance.date_assembly = validated_data.get('date_assembly', instance.date_assembly)
        instance.of_enterprise = validated_data.get('of_enterprise', instance.of_enterprise)

        instance.save()
        return instance
"""