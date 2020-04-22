from rest_framework import generics, request
from rest_framework.request import Request
from rest_framework.mixins import ListModelMixin
from .serialazers import CarSerializer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # миксин для доступа аутентифицированным пользователям
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from ..models import Car, Enterprise, User, Manager


class CarListView(LoginRequiredMixin, generics.ListAPIView, ListModelMixin):
    # визуализатор Llist для модели Car
    def get_queryset(self):
        user_name = self.request.user.username
        list_car = Car.objects.all()
        if user_name != 'admin':
            enterprise = Enterprise.objects.get(manager__username__contains=user_name)
            list_car = Car.objects.filter(of_enterprise=enterprise)
        return list_car


    queryset = get_queryset
    serializer_class = CarSerializer
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
