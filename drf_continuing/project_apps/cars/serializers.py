from rest_framework import serializers

from .models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для создания записи в Car"""
    class Meta:
        model = Car
        fields = '__all__'


class CarsListSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка машин"""
    class Meta:
        model = Car
        exclude = ('vin',)
