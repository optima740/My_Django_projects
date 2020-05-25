from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^test/$', views.TestUserViews, name='TestView'),
    url(r'^cars/$', views.CarView.as_view(), name='CarListView'),

    path('edit_cars/<int:pk>', views.EditCarView.as_view(), name='EditCar'),
    #path('cars/<int:pk>', views.SingleCarView.as_view(), name='SingleCarView'),

    url(r'^enterprise/$', views.EnterpriseView.as_view(), name='EnterpriseListView'),

    #url(r'^cars/$', views.CarDetailView.as_view(), name='CarDetailView'),
    # обработчик пути для cars

]