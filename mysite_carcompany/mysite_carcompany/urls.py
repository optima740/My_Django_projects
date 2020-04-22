from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path

from rest_framework import routers


router = routers.DefaultRouter()


urlpatterns = [
    path('', include('carcompany_app.urls')),
    url(r'^admin/', admin.site.urls),
    path('api/', include('carcompany_app.api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    ]
