from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator

class Customer(User):
    class Meta:
        # отрисовка имени в админ панели
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    award = models.FloatField(blank=True, default=0)

    def cashback(self, summ):
        self.award += summ
        self.save()

    def save(self, *args, **kwargs):
        self.award = round(self.award, 2)
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.first_name, self.last_name, self.phone, self.award)

class Pay(models.Model):
    class Meta:
        verbose_name = 'Pay'
        verbose_name_plural = 'Payments'
    author = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    validator = MinValueValidator(0.0)
    payment_summ = models.FloatField(validators=[validator], max_length=12)
    date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.payment_summ = round(self.payment_summ, 2)
        summ = self.payment_summ * 0.3
        self.author.cashback(summ)
        super(Pay, self).save(*args, **kwargs)

    def __str__(self):
        return '%s, %s, %s' % (self.author, self.payment_summ, self.date)

class Redemption(models.Model):
    class Meta:
        verbose_name = 'Redemption'
        verbose_name_plural = 'Redemptions'
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    payment_summ = models.FloatField(max_length=16, blank=True)
    create_data = models.DateTimeField(auto_now_add=True, auto_now=False)
    processing_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.BooleanField(default=False, blank=True)
    account_number = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.customer, self.payment_summ, self.create_data, self.processing_date,
                                           self.status, self.account_number)