from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .views import *
from .models import *
from django.conf.urls import url
from django.urls import path

class CustomerAdmin(admin.ModelAdmin):

    class Meta:
        model = Customer
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'award']
    #fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'award']
    user_fields = ['first_name', 'last_name', 'email', 'phone', 'award']
    superuser_fields = ['username', 'password']
    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.fields = self.user_fields + self.superuser_fields
        else:
            self.fields = self.user_fields

        return super(CustomerAdmin, self).get_form(request, obj, **kwargs)


class PayAdmin(admin.ModelAdmin):

    class Meta:
        model = Pay
    list_display = ['author', 'payment_summ', 'date']

class RepaymentAdmin(admin.ModelAdmin):
    class Meta:
        model = Repayment
    list_display = ['customer', 'payment_summ', 'create_data', 'processing_date', 'status', 'account_number']
    #actions = ['get_repayment']

    def get_form(self, request, obj=None, **kwargs):
        readonly = ['customer', 'payment_summ', 'create_data', 'processing_date', 'status', 'account_number']
        if Repayment.status == False:
            self.readonly_fields = readonly
        return super(RepaymentAdmin, self).get_form(request, obj, **kwargs)

    def get_urls(self):
        urls = super(RepaymentAdmin, self).get_urls()
        custom_urls = [
            path('get/', self.admin_site.admin_view(self.get_repayment), name='repayment_view'), ]
        return  custom_urls + urls

    def get_repayment(self, request):
        username = request.user.username
        customer = Customer.objects.get(username=username)
        sizepay = 0
        message = ''
        if request.method == 'POST':
            sizepay = request.POST.get('sizepay')
            if float(sizepay) <= float(customer.award):
                customer.change_balance(float(sizepay))
                Repayment.objects.create(customer=customer, payment_summ=float(sizepay), status=True)
                message = 'Operation successfully!'
            else:
                message = 'Operation error: insufficient balance'
        result = {'username': username, 'balance': customer, 'sizepay': sizepay, 'message': message}
        return render(request, 'index.html', locals())
    change_form_template = 'admin/myapp/repayment/my_change_form.html'

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Pay, PayAdmin)
admin.site.register(Repayment, RepaymentAdmin)

