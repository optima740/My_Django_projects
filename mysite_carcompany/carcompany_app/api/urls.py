from django.conf.urls import url
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/api/cars
    url(r'^cars/$', views.CarListView.as_view(), name='Car_list'),
    url(r'^cars/$', views.CarDetailView.as_view(), name='Car_detail'),
]