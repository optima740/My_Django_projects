# Generated by Django 3.0.4 on 2020-04-01 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carcompany_app', '0003_car_enterprise'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carcompany_app.Car'),
        ),
        migrations.AddField(
            model_name='driver',
            name='status_for_car',
            field=models.CharField(choices=[('Truck', 'Truck driver'), ('Car', 'Passenger car')], default='Car', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='enterprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carcompany_app.Enterprise'),
        ),
    ]
