from django.contrib import admin
from .models import *



class DriverAdmin(admin.ModelAdmin):

    class Meta:
        model = Driver
    list_display = ['first_name', 'last_name', 'of_enterprise', 'car', 'status_for_car']

class ManagerAdmin(admin.ModelAdmin):

    class Meta:
        model = Manager
    list_display = ['first_name', 'last_name', 'of_enterprise', 'department']

class CarAdmin(admin.ModelAdmin):
    class Meta:
        model = Car

    list_display = ['brand', 'model', 'of_enterprise', 'date_of_buy']
    list_filter = ['of_enterprise']
    search_fields = ['model']

class TripAdmin(admin.ModelAdmin):
    class Meta:
        model = Trip

    list_display = ['geo_data', 'to_car', 'begin_time', 'save_time', 'end_time']

admin.site.register(Driver, DriverAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Enterprise)
admin.site.register(Car, CarAdmin)
admin.site.register(Trip, TripAdmin)
# Register your models here.

