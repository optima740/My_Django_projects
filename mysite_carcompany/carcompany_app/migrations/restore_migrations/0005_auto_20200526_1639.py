# Generated by Django 3.0.4 on 2020-05-26 12:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('carcompany_app', '0004_auto_20200526_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='date_assembly',
        ),
        migrations.AddField(
            model_name='car',
            name='date_of_buy',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 26, 12, 39, 29, 187745, tzinfo=utc)),
        ),
    ]