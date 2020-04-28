from rest_framework import generics, request
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from .serialazers import CarSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # миксин для доступа аутентифицированным пользователям
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from ..models import Car, Enterprise, User, Manager


class CarListView(LoginRequiredMixin,  generics.ListAPIView, ):
    # визуализатор Llist для модели Car
    serializer_class = CarSerializer
    def get_queryset(self):
        # переопределяем родительский метод для запроса из БД с фильтром для наших условий
        user_name = self.request.user.username
        list_car = Car.objects.all()
        if user_name != 'admin':
            enterprise = Enterprise.objects.get(manager__username__contains=user_name)
            list_car = Car.objects.filter(of_enterprise=enterprise)
        return list_car

    def get(self, request):
        # переопределяем родительский метод для получения запроса GET
        queryset = self.get_queryset()
        serializer = CarSerializer(queryset, many=True)
        return Response({"cars": serializer.data})

    def post(self, request):
        # метод POST для создания новой Car.
        car = request.data.get('new_car') # получаем пользовательские данные из запроса по ключю "car"
        serializer = CarSerializer(data=car)
        # сериалайзер, как воод-вывод для взаимодействия с моделью Car. (создание)
        if serializer.is_valid(raise_exception=True): # проверка валидности данных из запроса с полями модели.
            car_saved = serializer.save()
        return Response({"success": "Car '{}' created successfully".format(car_saved)})

    def put(self,request, pk):
        saved_article = get_object_or_404(Car.objects.all(), pk=pk)
        data = request.data.get('car')
        serializer = CarSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            car_saved = serializer.save()
        return Response({"success": "Car '{}' updated successfully".format(car_saved)})


    raise_exception = True  # переопределение поля исключения, в случае не аутентифицированного пользователя

class CarDetailView(LoginRequiredMixin, generics.ListAPIView, ListModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    raise_exception = True  # переопределение поля исключения, в случае не аутентифицированного пользователя

from django.shortcuts import render


def TestUserViews(request):

    user_name = request.user.username
    manager = Manager.objects.filter(username=user_name)
    enterprise = Enterprise.objects.get(manager__username__contains=user_name)
    context = {
        'username': request.user.username,
        'manager': manager,
        'enterprise': enterprise
        #'enterprise': enterprise,

    }
    return render(request, 'Test.html', context)
