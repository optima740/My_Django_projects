from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from rest_framework.mixins import ListModelMixin

from .models import *



def redemption_view(request):
    username = Redemption.customer.username
    balance = Redemption.customer.award
    result = {'username': username, 'balance': balance}
    return render(request, 'index.html', result)

