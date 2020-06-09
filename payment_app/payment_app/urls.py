from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from django.conf.urls import url

urlpatterns = [
    path('', include('myapp.urls')),
    url(r'^admin/', admin.site.urls),

]
