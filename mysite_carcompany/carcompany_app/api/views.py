from rest_framework import generics
from .serialazers import CarSerializer
from django.shortcuts import get_object_or_404 # обработка исключений в случае ошибки
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication # для обработки аутентификации
from rest_framework.permissions import IsAuthenticated # для добавления разрешений для представлений
from ..models import Car, Enterprise

class CarListView(generics.ListAPIView):
    # визуализатор Llist для модели Car
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class EnterpriseEnrollView(APIView):
    # представление класса APIView для добавления сотрудников в предприятие (enterprise)
    authentication_classes = (BasicAuthentication,) # базовая аутентификация для сотрудников
    permission_classes = (IsAuthenticated,) # запрет доступа анонимных пользователей (не прошедших аутентификацию) к
    # данному представлению (классу)
    

    def post(self, request, pk, format=None):
        # для обработки POST запроса. Для данного метода запрещены все остальные глаголы HTTP, кроме POST
        # ожидаем идентификатор предприятия (enterprise) pk, находим предприятие по данноу идентификатору.
        enterprise = get_object_or_404(Enterprise, pk=pk) # если предприятие не найдено по pk, вызывается исключение 404.
        enterprise.managers.add(request.user)
        return Response({'enrolled': True})

