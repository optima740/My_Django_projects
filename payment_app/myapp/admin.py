from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .views import *
from .models import *
from django.conf.urls import url

class CustomerAdmin(admin.ModelAdmin):

    class Meta:
        model = Customer
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'award']
    fields = ['first_name', 'last_name', 'email', 'phone', 'award']

class PayAdmin(admin.ModelAdmin):

    class Meta:
        model = Pay
    list_display = ['author', 'payment_summ', 'date']

class RedemptionAdmin(admin.ModelAdmin):
    class Meta:
        model = Redemption

    list_display = ['customer', 'payment_summ', 'create_data', 'processing_date', 'status', 'account_number']
    actions = ['get_redemption']



    def get_redemption(self, request, quryset):

        username = 'AA'
        balance = 1000
        result = {'username': username, 'balance': balance}
        return render(request, 'index.html', locals())
    get_redemption.short_description = 'Выплата'
    #get_redemption.allowed_permissions = ('change', )
    """
    def get_urls(self):
        urls = super(RedemptionAdmin, self).get_urls()
        custom_urls = [
            url('^/redemption-to/$', self.admin_site.admin_view(redemption_view), name='redemption'), ]
        return custom_urls + urls
    
    def redemption_btmp(self, request):

        #import_custom = ImportCustom()
        #count = import_custom.import_data()

        username = Redemption.customer.username
        balance = Redemption.customer.award
        result = {'username': username, 'balance': balance}
        self.message_user(request, f"OK!!!!!!!")
        return render(request, 'index.html', result)

        #return HttpResponseRedirect("../")
    """
    change_form_template = 'admin/myapp/redemption/my_change_form.html'





admin.site.register(Customer, CustomerAdmin)
admin.site.register(Pay, PayAdmin)
admin.site.register(Redemption, RedemptionAdmin)

