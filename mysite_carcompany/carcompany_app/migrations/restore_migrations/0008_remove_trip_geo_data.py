# Generated by Django 3.0.4 on 2020-06-04 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carcompany_app', '0007_auto_20200604_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='geo_data',
        ),
    ]
