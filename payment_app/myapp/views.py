from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from rest_framework.mixins import ListModelMixin

from .models import *



def redemption_view(request):
    username = 'AA'
    balance = 1000
    sizepay = ''
    if request.method == 'POST':
        sizepay = request.POST.get('sizepay')

    #sizepay = request.POST.get('sizepay')
    result = {'username': username, 'balance': balance, 'sizepay': sizepay }
    return render(request, 'index.html', locals())

