from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cars/$', views.CarListView.as_view(), name='CarListView'),
    url(r'^cars/$', views.CarDetailView.as_view(), name='CarDetailView'),
    # обработчик пути для cars
    url(r'^enterprise/(?P<pk>\d+)/enroll/$', views.EnterpriseEnrollView.as_view(), name='Enterprise_enroll'),
    # обработчик пути для POST запроса на рдобавление менеджера в Enterprise
]