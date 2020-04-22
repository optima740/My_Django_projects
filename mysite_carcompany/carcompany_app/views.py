from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Car
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required # декораторы для форм login
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')





