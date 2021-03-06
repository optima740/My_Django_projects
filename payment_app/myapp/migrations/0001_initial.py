# Generated by Django 3.0.4 on 2020-06-08 19:48

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('award', models.CharField(blank=True, default=0, max_length=5)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Redemption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_summ', models.FloatField(blank=True, max_length=5)),
                ('create_data', models.DateTimeField(auto_now=True)),
                ('processing_date', models.DateTimeField()),
                ('status', models.BooleanField(blank=True, default=False)),
                ('account_number', models.CharField(max_length=32)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Customer')),
            ],
            options={
                'verbose_name': 'Redemption',
                'verbose_name_plural': 'Redemptions',
            },
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_summ', models.FloatField(max_length=5, verbose_name=django.core.validators.MinValueValidator(0.0))),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Customer')),
            ],
            options={
                'verbose_name': 'Pay',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]
