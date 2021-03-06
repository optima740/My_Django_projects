import time

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.gis.db import models as model_gis
import datetime
from django.utils.timezone import now, pytz

class Enterprise(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    title = models.CharField(max_length=32)
    address = models.CharField(max_length=64)
    time_zone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    def __str__(self):
        return '%s, %s, %s' % (self.title, self.address, self.time_zone)

class Car(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    fuel_util = models.CharField(max_length=5)
    date_of_buy = models.DateTimeField(auto_now=True)
    of_enterprise = models.ForeignKey('Enterprise', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s, %s' % (self.brand, self.model)

class Driver(User):
    class Meta:
        # отрисовка имени в админ панели
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    #age = models.CharField(max_length=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    CATEGORY_CHOICES = (('Truck', 'Truck driver'), ('Car', 'Passenger car'), )
    STATUS_CHOICES = (('ACT', 'Active'), ('NO_ACT', 'No active'), )
    specialization = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='Car')
    status_for_car = models.CharField(max_length=6, choices=STATUS_CHOICES, default='NO_ACT')
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    of_enterprise = models.ForeignKey('Enterprise', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return '%s, %s, %s, %s, %s' % (self.first_name, self.last_name, self.specialization, self.car, self.status_for_car)

class Manager(User):
    class Meta:
        # отрисовка имени в админ панели
        verbose_name = 'Manager'
        verbose_name_plural = 'Managers'

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    #age = models.CharField(max_length=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    DEPARTMENT_CHOICES = (('F', 'Finance department'), ('T', 'Technical department'), ('A', 'Administrate department'), )
    department = models.CharField(max_length=1, choices=DEPARTMENT_CHOICES, default='A')
    of_enterprise = models.ForeignKey('Enterprise', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return '%s, %s, %s' % (self.first_name, self.last_name, self.of_enterprise)

class Trip(model_gis.Model):
    # поездка, привязана к автомобилю
    geo_data = models.FileField(upload_to='geo_tracks/%Y/%m/%d', null=True, blank=True,)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField()
    save_time = models.DateTimeField(auto_now=True)
    to_car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)