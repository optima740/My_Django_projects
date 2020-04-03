from django.conf import settings
from django.db import models
from django.utils import timezone

class Enterprise(models.Model):
    title = models.CharField(max_length=32)
    address = models.CharField(max_length=64)

    def __str__(self):
        return self.title

class User(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    enterprise = models.ForeignKey('Enterprise', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    color = models.CharField(max_length=16)
    fuel_util = models.FloatField(max_length=3)
    date_assembly = models.DateField(auto_now_add=True)
    enterprise = models.ForeignKey('Enterprise', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s, %s' % (self.brand, self.model)

class Driver(User):
    CATEGORY_CHOICES = (('Truck', 'Truck driver'), ('Car', 'Passenger car'), )
    STATUS_CHOICES = (('ACT', 'Active'), ('NO_ACT', 'No active'), )
    specialization = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='Car')
    status_for_car = models.CharField(max_length=6, choices=STATUS_CHOICES, default='NO_ACT')
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.name, self.specialization, self.car, self.status_for_car)

class Manager(User):
    DEPARTMENT_CHOICES = (('F', 'Finance department'), ('T', 'Technical department'), ('A', 'Administrate department'), )
    department = models.CharField(max_length=1, choices=DEPARTMENT_CHOICES, default='A')

    def __str__(self):
        return '%s, %s' % (self.name, self.department)
