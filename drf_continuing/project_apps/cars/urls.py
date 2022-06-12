from django.urls import path, include

from .views import index, CarCreateView, CarListView, CarDetailView

urlpatterns = [
    path('', index),
    path('create/', CarCreateView.as_view()),   # http://127.0.0.1:8000/api/v1/cars/create/
    path('list/', CarListView.as_view()),   # http://127.0.0.1:8000/api/v1/cars/list/
    path('detail/<int:pk>/', CarDetailView.as_view()),   # http://127.0.0.1:8000/api/v1/cars/detail/4
]
