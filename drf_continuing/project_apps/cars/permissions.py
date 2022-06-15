"""
Создаем свои permissions
туториал по permissions: https://www.django-rest-framework.org/api-guide/permissions/
туториал по созданию своих: https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions

Все классы permissions наследуются от базового класса BasePermissions, и в нем определены 2 метода:



class BasePermissions(metaclass=BasePermissionMetaclass):
    def has_permission(self, request, view):
        '''позволяет настраивать права доступа на уровне всего доступа от клиента'''
        return True
    def has_object_permission(self, request, view, obj):
        '''позволяет настраивать права доступа на уровне отдельного объекта записи БД'''
        return True

Коллекция permissions.SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') - коллекция безопасных методов, т.е. только для чтения
"""

from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """кастомный пермишн, позволяющий просматривать данные, но изменять их может только администратор"""
    def has_permission(self, request, view):    # делаем ограничение прав доступа на уровне всего запроса
        if request.method in permissions.SAFE_METHODS:  # проверяем, "если пришедший запрос безопасен"
            return True     # если метод запроса в перечне коллекции SAFE_METHODS - то доступ для всех
        return bool(request.user and request.user.is_staff)  # если небезопасный - то только зарегистрированным и с True в поле is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта, позволяющее редактировать его только владельцам объекта.
    Т.е. только создатель объекта может внести изменения.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
