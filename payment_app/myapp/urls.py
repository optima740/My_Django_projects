from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
            url(r'^admin/myapp/redemption/redemption_to$', redemption_view, name='redemption'), ]
