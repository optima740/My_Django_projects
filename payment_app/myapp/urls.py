from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
            url(r'get/', redemption_view, name='view'),
    ]
