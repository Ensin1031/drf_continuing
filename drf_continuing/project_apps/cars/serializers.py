from rest_framework import serializers

from .models import Car


class CarDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для создания записи в Car"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'


class CarsListSerializer(serializers.ModelSerializer):
    """Сериализатор для вывода списка машин"""
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Car
        exclude = ('vin',)


"""
HiddenField(default= ) - скрытое поле  serializers.CurrentUserDefault() - вставляет по дефолту пользователя из реквеста
StringRelatedField(read_only=True)
SlugRelatedField(read_only=True, slug_field='username')
"""