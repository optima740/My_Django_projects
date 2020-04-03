from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #path(r'^api/', include('carcompany_app.api.urls', namespace='carcompany_app'))
    #http://127.0.0.1:8000/api/cars
    path('api/', include('carcompany_app.api.urls'))
    ]
