from django.shortcuts import render
from rest_framework import generics

from .models import Car
from .serializers import CarDetailSerializer, CarsListSerializer


def index(request):
    return render(request, 'cars/index.html', {'title': 'Hello, cars'})


"""
config breadcrambs
        context['breadcrumbs'] = (
            {'position': 1, 'name': 'Главная', 'url': 'home', 'resolved': True},
            {'position': 2, 'name': 'Все отзывы', 'url': 'reviews', 'resolved': True},
            {'position': 3, 'name': 'Добавить отзыв', 'resolved': False},
        )

"""


class CarCreateView(generics.CreateAPIView):
    """Создание записи в модели Car"""
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsListSerializer


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer


"""
CreateAPIView (serializer_class =) - создание записи в БД
ListAPIView (queryset =, serializer_class =) - просмотр всех записей в БД по кверисету
ListCreateAPIView (queryset =, serializer_class =) - просмотр всех записей БД по кверисету и создание записи

RetrieveUpdateDestroyAPIView (queryset =, serializer_class =) - позволяет осуществлять весь перечень действий по CRUD с 1 объектом
"""
