# Generated by Django 3.0.4 on 2020-04-01 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carcompany_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterprise',
            name='cars',
        ),
        migrations.RemoveField(
            model_name='enterprise',
            name='employee',
        ),
    ]
