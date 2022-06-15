from django.shortcuts import render
from rest_framework import generics
# from rest_framework import permissions

from .models import Car
from .serializers import CarDetailSerializer, CarsListSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


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
    permission_classes = (IsAdminOrReadOnly,)


class CarListView(generics.ListAPIView):
    """Просмотр всех записей, по кверисету"""
    queryset = Car.objects.all()
    serializer_class = CarsListSerializer


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование и удаление одной записи"""
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    permission_classes = (IsOwnerOrReadOnly,)


"""
CreateAPIView (serializer_class =) - создание записи в БД
ListAPIView (queryset =, serializer_class =) - просмотр всех записей в БД по кверисету
ListCreateAPIView (queryset =, serializer_class =) - просмотр всех записей БД по кверисету и создание записи

RetrieveUpdateDestroyAPIView (queryset =, serializer_class =) - позволяет осуществлять весь перечень действий по CRUD с 1 объектом
"""


"""     Пермишны
туториал: https://www.django-rest-framework.org/api-guide/permissions/
Ограничение доступа (permissions):
permissions.AllowAny - полный доступ - дефолтное значение, если ничего не указано
permissions.IsAuthenticated - только для авторизированных пользователей
permissions.IsAdminUser - только для администраторов
permissions.IsAuthenticatedOrReadOnly - только для авторизированных или всем, но для чтения
"""

