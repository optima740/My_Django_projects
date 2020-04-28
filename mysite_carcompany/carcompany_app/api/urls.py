from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.TestUserViews, name='TestView'),
    url(r'^cars/$', views.CarListView.as_view(), name='CarListView'),
    url(r'^cars/<int:pk>', views.CarListView.as_view(), name='CarListView'),
    # url(r'^cars/$', views.CarDetailView.as_view(), name='CarDetailView'),
    # обработчик пути для cars

]